"""JSON utilities.py"""
import binascii
import codecs
import time
import sys
import os
import re
import glob
import json
import datetime
import keyword

from threading import Thread
from pymongo import MongoClient, ASCENDING, DESCENDING
from pymongo.errors import OperationFailure as PyMongoOperationFailed
from bson import ObjectId
from bson.timestamp import Timestamp
from bson.errors import InvalidId

from .osid.osid_errors import NullArgument, NotFound,\
    OperationFailed, Unimplemented, IllegalState, InvalidArgument
from dlkit.primordium.calendaring.primitives import DateTime
from dlkit.primordium.id.primitives import Id
from dlkit.primordium.type.primitives import Type
from importlib import import_module

from . import JSON_CLIENT

from . import types
PHANTOM_ROOT_IDENTIFIER = '000000000000000000000000'

# VMAP = {
#     'i': 'new',
#     'u': 'changed',
#     'd': 'deleted'
# }


# =======================================
# This is for the Filesystem version of the JSON build
# http://pythonhosted.org/PyInstaller/runtime-information.html#run-time-information
if getattr(sys, 'frozen', False):
    BOOTLOADER = True
    PROJECT_PATH = os.path.dirname(sys.executable)
else:
    BOOTLOADER = False
    PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))
# =======================================


class Filler(object):
    pass

# =======================================
# MyIterator and ListFiller classes are for the Filesystem based impl


class MyIterator(object):
    def __init__(self, data):
        # make sure ._data is an iterator, otherwise next(self._data) will fail
        self._data = iter(data)
        self._i = -1

    def __iter__(self):
        try:
            yield next(self._data)
        except AttributeError:
            self._i += 1
            if len(self._data) > 0 and self._i < len(self._data):
                yield self._data[self._i]
            else:
                raise StopIteration

    def next(self):
        try:
            return next(self._data)
        except AttributeError:
            self._i += 1
            if len(self._data) > 0 and self._i < len(self._data):
                return self._data[self._i]
            else:
                raise StopIteration

    __next__ = next


class ListFiller(object):
    def __init__(self, data):
        self._data = data

    def __iter__(self):
        return MyIterator(self._data)

    def count(self, *args):
        try:
            return self._data.available()
        except AttributeError:
            return len(self._data)

    def sort(self, *args, **kwargs):
        return self._data


# These helper methods are for the Filesystem impl
def clean_up_datetime(obj_map):
    """convert datetime objects to dictionaries for storage"""
    clean_map = {}
    for key, value in obj_map.items():
        if isinstance(value, datetime.datetime):
            clean_map[key] = {
                'year': value.year,
                'month': value.month,
                'day': value.day,
                'hour': value.hour,
                'minute': value.minute,
                'second': value.second,
                'microsecond': value.microsecond,
                'tzinfo': value.tzinfo
            }
        elif isinstance(value, dict):
            clean_map[key] = clean_up_datetime(value)
        elif isinstance(value, list):
            if key not in clean_map:
                clean_map[key] = []
            if len(value) > 0:
                for index, list_value in enumerate(value):
                    if isinstance(list_value, dict):
                        clean_map[key].append(clean_up_datetime(list_value))
                    else:
                        clean_map[key].append(list_value)
            else:
                clean_map[key] = value
        else:
            clean_map[key] = value
    return clean_map


def clean_up_embedded_object_ids(obj_map):
    clean_map = {}
    for key, value in obj_map.items():
        if isinstance(value, ObjectId):
            clean_map[key] = str(value)
        elif isinstance(value, dict):
            clean_map[key] = clean_up_embedded_object_ids(value)
        elif isinstance(value, list):
            new_list = []
            for internal_item in value:
                if isinstance(internal_item, dict):
                    new_list.append(clean_up_embedded_object_ids(internal_item))
                else:
                    new_list.append(internal_item)
            clean_map[key] = new_list
        else:
            clean_map[key] = value
    return clean_map


def convert_dict_to_datetime(obj_map):
    """converts dictionary representations of datetime back to datetime obj"""
    converted_map = {}
    for key, value in obj_map.items():
        if isinstance(value, dict) and 'tzinfo' in value.keys():
            converted_map[key] = datetime.datetime(**value)
        elif isinstance(value, dict):
            converted_map[key] = convert_dict_to_datetime(value)
        elif isinstance(value, list):
            updated_list = []
            for internal_item in value:
                if isinstance(internal_item, dict):
                    updated_list.append(convert_dict_to_datetime(internal_item))
                else:
                    updated_list.append(internal_item)
            converted_map[key] = updated_list
        else:
            converted_map[key] = value
    return converted_map


def convert_ids_to_object_ids(obj_map):
    """converts string representations of _id back to ObjectId obj"""
    converted_map = {}
    for key, value in obj_map.items():
        if key == '_id':
            # hacky, but using alias sends back the whole ID string, like
            #   assessment.Item%3A5758326b4a40452d6eee1fa1%40ODL.MIT.EDU
            # so we have to preserve it
            try:
                converted_map[key] = ObjectId(value)
            except InvalidId:
                converted_map[key] = value
        elif isinstance(value, dict):
            converted_map[key] = convert_ids_to_object_ids(value)
        elif isinstance(value, list):
            new_list = []
            for internal_item in value:
                if isinstance(internal_item, dict):
                    new_list.append(convert_ids_to_object_ids(internal_item))
                else:
                    new_list.append(internal_item)
            converted_map[key] = new_list
        else:
            converted_map[key] = value
    return converted_map


def fix_reserved_word(word, is_module=False):
    """
    Replaces words that may be problematic

    In particular the term 'type' is used in the osid spec, primarily as an argument
    parameter where a type is provided to a method.  'type' is a reserved word
    in python, so we give ours a trailing underscore. If we come across any other
    osid things that are reserved word they can be dealt with here.

    Copied from the builder binder_helpers.py file

    """
    if is_module:
        if word == 'logging':
            word = 'logging_'  # Still deciding this
    else:
        if keyword.iskeyword(word):
            word += '_'
        elif word in ['id', 'type', 'str', 'max', 'input', 'license', 'copyright', 'credits', 'help']:
            word += '_'
    return word


def is_string(string_):
    try:
        # python 2
        return isinstance(string_, basestring)
    except NameError:
        # python 3
        return isinstance(string_, str)


def query_is_match(query, contents):
    num_keys = len(list(query.keys()))
    num_matches = 0
    for key, value in query.items():
        if key == '_id' and isinstance(value, ObjectId):
            value = str(value)

        if isinstance(value, dict) and list(value.keys())[0] in ['$in', '$nin']:
            value_key = list(value.keys())[0]

            mod_value = value[value_key]
            matches_already_calculated = False
            if isinstance(value[value_key], list) and len(value[value_key]) > 0:
                if isinstance(value[value_key][0], ObjectId):
                    mod_value = [str(v) for v in value[value_key]]
                elif isinstance(value[value_key][0], re._pattern_type):
                    # then we need to do a regex comparison on the content value
                    regex = value[value_key][0]
                    if '.' in key:
                        # assume two levels deep?
                        haystack = contents[key.split('.')[0]][key.split('.')[1]]
                    else:
                        haystack = contents[key]
                    regex_key = list(value.keys())[0]
                    if regex_key == '$in':
                        if regex.search(haystack):
                            num_matches += 1
                    elif regex_key == '$nin':
                        if regex.search(haystack) is None:
                            num_matches += 1
                    matches_already_calculated = True

            if not matches_already_calculated:
                if '.' in key:
                    key_chain = key.split('.')
                    # assume only two levels deep for most basic use cases...
                    if key_chain[0] in contents:
                        sub_content = contents[key_chain[0]]
                        if isinstance(sub_content, list):
                            if not isinstance(key_chain[1], int):
                                for ele in sub_content:
                                    test_case = ele
                                    test_key = key_chain[1]

                                    if any(v2 in test_case[test_key] for v2 in mod_value):
                                        num_matches += 1
                            else:
                                test_case = sub_content[key_chain[1]]
                                test_key = key_chain[2]

                                if any(v2 in test_case[test_key] for v2 in mod_value):
                                    num_matches += 1
                        else:
                            test_case = sub_content
                            test_key = key_chain[1]

                            if test_case is not None and any(v2 in test_case[test_key] for v2 in mod_value):
                                num_matches += 1
                else:
                    if key in contents and any(v2 in contents[key] for v2 in mod_value):
                        num_matches += 1
            else:
                if key in contents and any(v2 in contents[key] for v2 in mod_value):
                    num_matches += 1
        elif '.' in key:
            key_chain = key.split('.')
            # assume only two levels deep for most basic use cases...
            if '_id' in key_chain:
                value = str(value)
            if key_chain[0] in contents:
                sub_content = contents[key_chain[0]]
                if isinstance(sub_content, list):
                    if not isinstance(key_chain[1], int):
                        for ele in sub_content:
                            test_case = ele
                            test_key = key_chain[1]

                            if test_case[test_key] == value:
                                num_matches += 1
                    else:
                        test_case = sub_content[key_chain[1]]
                        test_key = key_chain[2]

                        if test_case[test_key] == value:
                            num_matches += 1
                else:
                    test_case = sub_content
                    test_key = key_chain[1]

                    if test_case is not None and test_case[test_key] == value:
                        num_matches += 1
        elif (key in contents and
              isinstance(contents[key], list) and
              is_string(value)):
            if key in contents and value in contents[key]:
                num_matches += 1
        else:
            if key in contents and contents[key] == value:
                num_matches += 1
    return num_keys == num_matches


def splice_and_query(query):
    if '$and' in list(query.keys()):
        new_query = {}
        for item in query['$and']:
            new_query.update(item)
        return new_query
    else:
        return query
# =======================================


def set_json_client(runtime):
    # Default impl is MongoDB, but need to check if using Filesystem
    try:
        use_filesystem_param_id = Id('parameter:useFilesystem@json')
        use_filesystem = runtime.get_configuration().get_value_by_parameter(use_filesystem_param_id).get_boolean_value()
        if not use_filesystem:
            raise AttributeError()
    except (AttributeError, KeyError, NotFound):
        try:
            mongo_host_param_id = Id('parameter:mongoHostURI@json')
            mongo_host = runtime.get_configuration().get_value_by_parameter(mongo_host_param_id).get_string_value()
        except (AttributeError, KeyError, NotFound):
            JSON_CLIENT.set_json_client(MongoClient())
        else:
            JSON_CLIENT.set_json_client(MongoClient(mongo_host))
    else:
        JSON_CLIENT.set_json_client(True)


class JSONClientValidated(object):
    """automatically validates the insert_one, find_one, and delete_one methods"""
    def __init__(self, db, collection=None, runtime=None):
        if not JSON_CLIENT.is_json_client_set() and runtime is not None:
            set_json_client(runtime)

        self._json_impl = 'mongo'
        try:
            use_filesystem_param_id = Id('parameter:useFilesystem@json')
            use_filesystem = runtime.get_configuration().get_value_by_parameter(use_filesystem_param_id).get_boolean_value()
            if not use_filesystem:
                raise AttributeError()
        except (AttributeError, KeyError, NotFound):
            pass
        else:
            self._json_impl = 'filesystem'

        if self._impl('filesystem'):
            host_path = PROJECT_PATH
            try:
                host_path_param_id = Id('parameter:dataStorePath@json')
                if BOOTLOADER:
                    host_path = '{0}/{1}'.format(host_path,
                                                 runtime.get_configuration().get_value_by_parameter(host_path_param_id).get_string_value())
                else:
                    host_path = runtime.get_configuration().get_value_by_parameter(host_path_param_id).get_string_value()
            except (AttributeError, KeyError, NotFound):
                pass
            if collection is None:
                self._cursor = '{}/{}'.format(host_path, db)
            else:
                self._cursor = '{}/{}/{}'.format(host_path, db, collection)

            if not os.path.isdir(self._cursor):
                os.makedirs(self._cursor)
        else:
            # use MongoDB as default
            db_prefix = ''
            try:
                db_prefix_param_id = Id('parameter:mongoDBNamePrefix@json')
                db_prefix = runtime.get_configuration().get_value_by_parameter(db_prefix_param_id).get_string_value()
            except (AttributeError, KeyError, NotFound):
                pass

            if collection is None:
                self._mc = JSON_CLIENT.json_client[db_prefix + db]
            else:
                self._mc = JSON_CLIENT.json_client[db_prefix + db][collection]
                # add the collection index, if available in the configs
                try:
                    mongo_indexes_param_id = Id('parameter:indexes@json')
                    mongo_indexes = runtime.get_configuration().get_value_by_parameter(mongo_indexes_param_id).get_object_value()
                    namespace = '{0}.{1}'.format(db, collection)
                    if namespace in mongo_indexes:
                        for field in mongo_indexes[namespace]:
                            self._mc.create_index(field)
                except (AttributeError, KeyError, NotFound):
                    pass

    @staticmethod
    def _get_file_contents_as_json(file_path):
        with codecs.open(file_path, 'rb', encoding='utf-8') as input_file:
            return json.loads(input_file.read())

    def _impl(self, impl):
        return self._json_impl == impl.lower()

    @staticmethod
    def _convert_to_dict(query):
        # For Filesystem impl
        try:
            return query._query_terms
        except AttributeError:
            return query

    @staticmethod
    def _save_dict_as_json_file(file_path, dict):
        with codecs.open(file_path, 'wb', encoding='utf-8') as output_file:
            output_file.write(json.dumps(dict))

    def _validate_write(self, result):
        if self._impl('filesystem'):
            if not os.path.isfile(result):
                raise OperationFailed(str(result))
        else:
            try:
                if not result.acknowledged or result.inserted_id is None:
                    # if (('writeErrors' in result and len(result['writeErrors']) > 0) or
                    #         ('writeConcernErrors' in result and len(result['writeConcernErrors']) > 0)):
                    raise OperationFailed(str(result))
            except AttributeError:
                # account for deprecated save() method
                if result is None:
                    raise OperationFailed('Nothing saved to database.')

    def count(self):
        if self._impl('filesystem'):
            return 0
        return self._mc.count()

    def delete_one(self, query):
        if self._impl('filesystem'):
            # does not support datetime queries
            results = 0
            query = self._convert_to_dict(query)
            for target_file in glob.iglob(self._cursor + '/*.json'):
                contents = self._get_file_contents_as_json(target_file)

                if query_is_match(query, contents):
                    os.remove(target_file)
                    results += 1
                    break

            if results == 0:
                raise NotFound(str(query) + ' returned None.')
            return results

        # Mongo impl as default
        try:
            result = self._mc.delete_one(query)
        except TypeError:
            result = self._mc.remove(query)
            if result is not None:
                returned_object = result
                result = Filler()
                result.deleted_count = returned_object['n']
        if result is None or result.deleted_count == 0:
            raise NotFound(str(query) + ' returned None.')
        return result

    def find(self, query=None):
        if self._impl('filesystem'):
            # does not support datetime finding
            results = []
            if query is None:
                for target_file in glob.iglob(self._cursor + '/*.json'):
                    results.append(self._get_file_contents_as_json(target_file))
            else:
                query = self._convert_to_dict(query)
                query = splice_and_query(query)
                if '_id' in list(query.keys()) and not isinstance(query['_id'], dict):
                    potential_file = '{0}/{1}.json'.format(self._cursor,
                                                           query['_id'])
                    if os.path.isfile(potential_file):
                        del query['_id']
                        contents = self._get_file_contents_as_json(potential_file)
                        if query_is_match(query, contents):
                            contents = convert_dict_to_datetime(contents)
                            contents = convert_ids_to_object_ids(contents)
                            results.append(contents)
                elif '_id' in query:
                    if '$in' in query['_id']:
                        for query_id in query['_id']['$in']:
                            potential_file = '{0}/{1}.json'.format(self._cursor,
                                                                   query_id)
                            if os.path.isfile(potential_file):
                                contents = self._get_file_contents_as_json(potential_file)
                                if query_is_match(query, contents):
                                    contents = convert_dict_to_datetime(contents)
                                    contents = convert_ids_to_object_ids(contents)
                                    results.append(contents)
                    else:
                        # not match
                        pass
                else:
                    for target_file in glob.iglob(self._cursor + '/*.json'):
                        contents = self._get_file_contents_as_json(target_file)

                        if query_is_match(query, contents):
                            contents = convert_dict_to_datetime(contents)
                            contents = convert_ids_to_object_ids(contents)
                            results.append(contents)

            results = ListFiller(results)
            return results

        # Mongo impl as default
        if query is None:
            return self._mc.find()
        else:
            return self._mc.find(query)

    def find_one(self, query):
        if self._impl('filesystem'):
            # does not support datetime finding
            results = None
            query = self._convert_to_dict(query)
            query = splice_and_query(query)
            if '_id' in list(query.keys()) or 'question._id' in query.keys():
                if '_id' in list(query.keys()):
                    id_key = '_id'
                else:
                    id_key = 'question._id'
                potential_file = '{0}/{1}.json'.format(self._cursor,
                                                       query[id_key])
                if os.path.isfile(potential_file):
                    del query[id_key]
                    contents = self._get_file_contents_as_json(potential_file)
                    if query_is_match(query, contents):
                        contents = convert_dict_to_datetime(contents)
                        contents = convert_ids_to_object_ids(contents)
                        results = contents
                else:
                    raise NotFound(str(query) + ' returned None. Path: ' + self._cursor)

            if results is None:
                for target_file in glob.iglob(self._cursor + '/*.json'):
                    contents = self._get_file_contents_as_json(target_file)

                    if query_is_match(query, contents):
                        contents = convert_dict_to_datetime(contents)
                        contents = convert_ids_to_object_ids(contents)
                        results = contents
                        break

            if results is None:
                raise NotFound(str(query) + ' returned None. Path: ' + self._cursor)
            return results

        # Mongo impl as default
        result = self._mc.find_one(query)
        if result is None:
            raise NotFound(str(query) + ' returned None.')
        return result

    def insert_one(self, doc):
        if self._impl('filesystem'):
            try:
                doc['_id'] = str(doc['_id'])  # to convert the ObjectID to a string
            except KeyError:
                doc['_id'] = str(ObjectId())

            doc = clean_up_datetime(doc)
            doc = clean_up_embedded_object_ids(doc)

            write_target = '{}/{}.json'.format(self._cursor,
                                               doc['_id'])
            self._save_dict_as_json_file(write_target, doc)

            self._validate_write(write_target)
            inserted_obj = Filler()
            inserted_obj.inserted_id = doc['_id']
            return inserted_obj

        # Mongo impl as default
        try:
            result = self._mc.insert_one(doc)
        except TypeError:
            # pymongo 2.8.1
            result = self._mc.insert(doc)
            if result is not None:
                returned_object_id = result
                result = Filler()
                result.inserted_id = returned_object_id
        self._validate_write(result)
        return result

    def raw(self):
        """ return the raw mongo client object...used for GridFS
        """
        if self._impl('filesystem'):
            return self._cursor

        return self._mc

    def save(self, doc):
        if self._impl('filesystem'):
            try:
                doc['_id'] = str(doc['_id'])  # to convert the ObjectID to a string
            except KeyError:
                doc['_id'] = str(ObjectId())

            doc = clean_up_datetime(doc)
            doc = clean_up_embedded_object_ids(doc)

            write_target = '{}/{}.json'.format(self._cursor,
                                               doc['_id'])

            self._save_dict_as_json_file(write_target, doc)
            self._validate_write(write_target)
            inserted_obj = Filler()
            inserted_obj.inserted_id = doc['_id']
            return inserted_obj

        # Mongo impl as default
        try:
            # pymongo 3
            result = self._mc.replace_one({'_id': doc['_id']}, doc, upsert=True)
        except TypeError:
            # pymongo 2
            result = self._mc.save(doc)
        self._validate_write(result)
        return result


def remove_null_proxy_kwarg(func):
    """decorator, to remove a 'proxy' keyword argument. For wrapping certain Manager methods"""
    def wrapper(*args, **kwargs):
        if 'proxy' in kwargs:
            # if kwargs['proxy'] is None:
            del kwargs['proxy']
            # else:
            #    raise InvalidArgument('Manager sessions cannot be called with Proxies. Use ProxyManager instead')
        return func(*args, **kwargs)
    return wrapper


def arguments_not_none(func):
    """decorator, to check if any arguments are None; raise exception if so"""
    def wrapper(*args, **kwargs):
        for arg in args:
            if arg is None:
                raise NullArgument()
        for arg, val in kwargs.items():
            if val is None:
                raise NullArgument()
        try:
            return func(*args, **kwargs)
        except TypeError as ex:
            if any(statement in ex.args[0] for statement in ['takes exactly',
                                                             'required positional argument']):
                raise NullArgument('Wrong number of arguments provided: ' + str(ex.args[0]))
            else:
                raise
    return wrapper


def handle_simple_sequencing(func):
    """decorator, deal with simple sequencing cases"""
    from .assessment import assessment_utilities

    def wrapper(*args, **kwargs):
        # re-order these things because have to delete the part after
        # removing it from the parent sequence map
        if 'create_assessment_part' in func.__name__:
            result = func(*args, **kwargs)
            assessment_utilities.update_parent_sequence_map(result)
        elif func.__name__ == 'delete_assessment_part':
            # args[1] is the assessment_part_id
            assessment_utilities.remove_from_parent_sequence_map(*args)
            result = func(*args, **kwargs)
        else:
            result = func(*args, **kwargs)
        return result
    return wrapper


def get_provider_manager(osid, runtime=None, proxy=None, local=False):
    """
    Gets the most appropriate provider manager depending on config.

    If local is True, then don't bother with the runtime/config and
    try to get the requested service manager directly from the local
    service implementations known to this mongodb implementation.

    """
    if runtime is not None:
        if local:
            parameter_id = Id('parameter:localImpl@json')
        else:
            parameter_id = Id('parameter:' + osid.lower() + 'ProviderImpl@json')
        try:
            # Try to get the manager from the runtime, if available:
            config = runtime.get_configuration()
            impl_name = config.get_value_by_parameter(parameter_id).get_string_value()
            if proxy is None:
                return runtime.get_manager(osid, impl_name)
            else:
                return runtime.get_proxy_manager(osid, impl_name)
        except (AttributeError, KeyError, NotFound):
            pass
    # Try to return a Manager directly from this implementation, or raise OperationFailed:
    try:
        if proxy is None:
            mgr_str = 'Manager'
        else:
            mgr_str = 'ProxyManager'
        module = import_module(
            'dlkit.json_.' + fix_reserved_word(osid.lower(), is_module=True) + '.managers')
        manager_name = ''.join((osid.title()).split('_')) + mgr_str
        manager = getattr(module, manager_name)()
    except (ImportError, AttributeError):
        raise OperationFailed()
    if runtime is not None:
        manager.initialize(runtime)
    return manager


def get_provider_session(provider_manager, session_method, proxy=None, *args, **kwargs):
    if proxy is None:
        return getattr(provider_manager, session_method)(*args, **kwargs)
    else:
        return getattr(provider_manager, session_method)(proxy, *args, **kwargs)

# Deprecated. Delete me:
# def format_catalog(catalog_name):
#     return catalog_name.replace('_', '').title()


def caps_to_mixed(caps_string):
    return caps_string[0].lower() + caps_string[1:]


def now_map():
    now = DateTime.utcnow()
    return {
        'year': now.year,
        'month': now.month,
        'day': now.day,
        'hour': now.hour,
        'minute': now.minute,
        'second': now.second,
        'microsecond': now.microsecond,
    }


def overlap(start1, end1, start2, end2):
    """
    Does the range (start1, end1) overlap with (start2, end2)?

    From Ned Batchelder
    http://nedbatchelder.com/blog/201310/range_overlap_in_two_compares.html

    """
    return not (end1 < start2 or end2 < start1)


class OsidListList(list):
    """
    A morker class for initializing OsidLists with a list of other OsidLists

    To use, load up this list with OsidLists of the same object type, and pass
    it as the argument to an OsidList of that same object type. The OsidList
    should exhaust all the contained OsidLists in order on iteration to return
    all the underlying objects as if they are part of one list.

    """
    pass


def get_registry(entry, runtime):
    """Returns a record registry given an entry and runtime"""
    try:
        records_location_param_id = Id('parameter:recordsRegistry@mongo')
        registry = runtime.get_configuration().get_value_by_parameter(
            records_location_param_id).get_string_value()
        return import_module(registry).__dict__.get(entry, {})
    except (ImportError, AttributeError, KeyError, NotFound):
        return {}


def is_authenticated_with_proxy(proxy):
    """Given a Proxy, checks whether a user is authenticated"""
    if proxy is None:
        return False
    elif proxy.has_authentication():
        return proxy.get_authentication().is_valid()
    else:
        return False


def get_authenticated_agent_id_with_proxy(proxy):
    """Given a Proxy, returns the Id of the authenticated Agent"""
    if is_authenticated_with_proxy(proxy):
        return proxy.get_authentication().get_agent_id()
    else:
        raise IllegalState()


def get_authenticated_agent_with_proxy(proxy):
    """Given a Proxy, returns the authenticated Agent"""
    if is_authenticated_with_proxy(proxy):
        return proxy.get_authentication().get_agent()
    else:
        raise IllegalState()


def get_effective_agent_id_with_proxy(proxy):
    """Given a Proxy, returns the Id of the effective Agent"""
    if is_authenticated_with_proxy(proxy):
        if proxy.has_effective_agent():
            return proxy.get_effective_agent_id()
        else:
            return proxy.get_authentication().get_agent_id()
    else:
        return Id(
            identifier='MC3GUE$T@MIT.EDU',
            namespace='authentication.Agent',
            authority='MIT-ODL')


def get_effective_agent_with_proxy(proxy):
    """Given a Proxy, returns the effective Agent"""
    # effective_agent_id = self.get_effective_agent_id()
    # This may want to be extended to get the Agent directly from the Authentication
    # if available and if not effective agent is available in the proxy
    # return Agent(
    #    identifier=effective_agent_id.get_identifier(),
    #    namespace=effective_agent_id.get_namespace(),
    #    authority=effective_agent_id.get_authority())
    raise Unimplemented()


def get_locale_with_proxy(proxy):
    """Given a Proxy, returns the Locale

    This assumes that instantiating a dlkit.mongo.locale.objects.Locale
    without constructor arguments wlll return the default Locale.

    """
    from .locale.objects import Locale
    if proxy is not None:
            locale = proxy.get_locale()
            if locale is not None:
                return locale
    return Locale()


def update_display_text_defaults(mdata, locale_map):
    for default_display_text in mdata['default_string_values']:
        default_display_text.update(locale_map)


def make_catalog_map(cat_name, identifier=PHANTOM_ROOT_IDENTIFIER, default_text='Default'):
    return ({
        '_id': ObjectId(identifier),
        'displayName': {'text': default_text + ' ' + cat_name,
                        'languageTypeId': str(Type(**types.Language().get_type_data('DEFAULT'))),
                        'scriptTypeId': str(Type(**types.Script().get_type_data('DEFAULT'))),
                        'formatTypeId': str(Type(**types.Format().get_type_data('DEFAULT'))), },
        'description': {'text': default_text + ' ' + cat_name,
                        'languageTypeId': str(Type(**types.Language().get_type_data('DEFAULT'))),
                        'scriptTypeId': str(Type(**types.Script().get_type_data('DEFAULT'))),
                        'formatTypeId': str(Type(**types.Format().get_type_data('DEFAULT'))), },
        'genusTypeId': str(Type(**types.Genus().get_type_data('DEFAULT'))),
        'recordTypeIds': []
    })


def camel_to_under(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


def convert_catalog_id_to_object_id_string(catalog_id):
    """When doing hierarchies, need to convert a catalogId into an
    ObjectId, so convert to a string, then into a hex format.

    i.e. Bank Assessment hierarchy should become
         BANKASSESSME
         '42414e4b4153534553534d45'
     """

    if not isinstance(catalog_id, Id):
        raise TypeError('input needs to be an Id')
    seed_str = catalog_id.get_identifier() + catalog_id.get_authority() + '000000000000'
    try:
        seed_str = str.encode(seed_str[:12])
    except TypeError:
        # sometimes unicode is returned, in which case Python 2 can't handle it
        seed_str = seed_str[:12]
    seed_str = binascii.hexlify(seed_str)
    try:
        # python 3
        seed_str = str(seed_str, 'utf8')
    except TypeError:
        # python 2
        seed_str = str(seed_str)
    return seed_str
