"""Records shared by all osid objects"""

from .base_records import ObjectInitRecord, QueryInitRecord, ProvenanceFormRecord
from dlkit.json_.osid import record_templates as osid_records
from dlkit.json_.osid.metadata import Metadata

from dlkit.abstract_osid.osid.errors import NoAccess
from dlkit.primordium.id.primitives import Id
from dlkit.primordium.type.primitives import Type

from .registry import OSID_OBJECT_RECORD_TYPES

ENCLOSURE_RECORD = Type(**OSID_OBJECT_RECORD_TYPES['enclosure'])

CATALOG_LOOKUP = {
    'assessment': 'bank',
    'repository': 'repository',
    'commenting': 'book',
    'learning': 'objective_bank',
}


class EnclosureRecord(ObjectInitRecord):
    """Record extension to wrap an enclosed foreign object"""

    def __init__(self, osid_object):
        self._enclosed_object = None
        super(EnclosureRecord, self).__init__(osid_object)
        if (not hasattr(self.my_osid_object, '_supported_record_type_ids') or
                self.my_osid_object._supported_record_type_ids is None):
            self.my_osid_object._supported_record_type_ids = []
        self.my_osid_object._supported_record_type_ids.append(
            str(ENCLOSURE_RECORD))

    def __getattr__(self, name):
        return getattr(self.get_enclosed_object, name)

    def get_display_name(self):
        """Overrides get_display_name of extended object"""
        return self.get_enclosed_object().get_display_name()

    display_name = property(fget=get_display_name)

    def get_description(self):
        """Overrides get_description of extended object"""
        return self.get_enclosed_object().get_description()

    description = property(fget=get_description)

    def get_genus_type(self):
        """Overrides get_genus_type of extended object"""
        enclosed_object_id = self.get_enclosed_object_id()
        package = enclosed_object_id.get_identifier_namespace().split('.')[0]
        obj = enclosed_object_id.get_identifier_namespace().split('.')[1]
        return Type(
            authority='OSID.ORG',
            namespace=package,
            identifier=obj,
            display_name=obj,
            display_label=obj,
            description=package + ' ' + obj + ' type',
            domain=package + '.' + obj)

    genus_type = property(fget=get_genus_type)

    def get_enclosed_object_id(self):
        """Return the osid Id of the enclosed object"""
        return Id(self.my_osid_object._my_map['enclosedObjectId'])

    enclosed_object_id = property(fget=get_enclosed_object_id)

    def get_enclosed_object(self):
        """Return the enclosed object"""
        if self._enclosed_object is None:
            enclosed_object_id = self.get_enclosed_object_id()
            package_name = enclosed_object_id.get_identifier_namespace().split('.')[0]
            obj_name = enclosed_object_id.get_identifier_namespace().split('.')[1]
            mgr = self.my_osid_object._get_provider_manager(package_name.upper())
            try:
                lookup_session = getattr(mgr, 'get_' + obj_name.lower() + '_lookup_session')(self.my_osid_object._proxy)
            except TypeError:
                lookup_session = getattr(mgr, 'get_' + obj_name.lower() + '_lookup_session')()
            getattr(lookup_session, 'use_federated_' + CATALOG_LOOKUP[package_name] + '_view')()
            self._enclosed_object = getattr(
                lookup_session, 'get_' + obj_name.lower())(enclosed_object_id)
        return self._enclosed_object

    enclosed_object = property(fget=get_enclosed_object)

    def clone_to(self, target_catalog):
        """need to clone both the enclosed object + the wrapping asset"""
        def _clone(obj_id):
            package_name = obj_id.get_identifier_namespace().split('.')[0]
            obj_name = obj_id.get_identifier_namespace().split('.')[1].lower()

            catalogs = {
                'assessment': 'bank',
                'repository': 'repository'
            }

            my_catalog_name = catalogs[package_name.lower()]

            mgr = self.my_osid_object._get_provider_manager(package_name.upper())

            catalog_lookup_session = getattr(mgr, 'get_' + my_catalog_name + '_lookup_session')()
            catalog = getattr(catalog_lookup_session, 'get_' + my_catalog_name)(target_catalog.ident)

            admin_session = getattr(mgr, 'get_' + obj_name + '_admin_session_for_' + my_catalog_name)(catalog.ident)

            new_obj = getattr(admin_session, 'duplicate_' + obj_name)(obj_id)
            try:
                form = getattr(admin_session, 'get_' + obj_name + '_form_for_update')(new_obj.ident)
                form.set_provenance(str(obj_id))
                new_obj = getattr(admin_session, 'update_' + obj_name)(form)
            except AttributeError:
                pass
            return new_obj
        enclosed_object_id = self.get_enclosed_object_id()
        new_enclosed_object = _clone(enclosed_object_id)

        # Let's do the asset here
        enclosure_id = self.my_osid_object.ident
        new_asset = _clone(enclosure_id)
        package_name = enclosure_id.get_identifier_namespace().split('.')[0]
        obj_name = enclosure_id.get_identifier_namespace().split('.')[1].lower()

        catalogs = {
            'assessment': 'bank',
            'repository': 'repository'
        }

        my_catalog_name = catalogs[package_name.lower()]

        mgr = self.my_osid_object._get_provider_manager(package_name.upper())

        catalog_lookup_session = getattr(mgr, 'get_' + my_catalog_name + '_lookup_session')()
        catalog = getattr(catalog_lookup_session, 'get_' + my_catalog_name)(target_catalog.ident)

        admin_session = getattr(mgr, 'get_' + obj_name + '_admin_session_for_' + my_catalog_name)(catalog.ident)
        form = getattr(admin_session, 'get_' + obj_name + '_form_for_update')(new_asset.ident)
        form.set_enclosed_object(new_enclosed_object.ident)
        return getattr(admin_session, 'update_' + obj_name)(form)


class EnclosureQueryRecord(QueryInitRecord):
    """for querying on enclosed objects"""

    def match_enclosed_object_id(self, object_id):
        """stub"""
        self._my_osid_query._add_match('enclosedObjectId', str(object_id), True)

    def clear_mecqbank_item_id(self):
        """stub"""
        self._my_osid_query._clear_terms('enclosedObjectId')


class EnclosureFormRecord(ProvenanceFormRecord, osid_records.OsidRecord):

    def __init__(self, osid_object_form=None):
        if osid_object_form is not None:
            self.my_osid_object_form = osid_object_form
        self._init_metadata()
        if not self.my_osid_object_form.is_for_update():
            self._init_map()
        super(EnclosureFormRecord, self).__init__()

    def _init_metadata(self):
        """Initialize metadata for this record"""
        self._enclosed_object_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'enclosed_object'),
            'element_label': 'Enclosed Object',
            'instructions': 'accepts an osid object Id',
            'required': False,
            'read_only': False,
            'linked': False,
            'array': False,
            'default_id_values': [''],
            'syntax': 'ID',
            'id_set': []
        }

    def _init_map(self):
        """Initialize osid objects _my_map for this record"""
        self.my_osid_object_form._my_map['enclosedObjectId'] = \
            self._enclosed_object_metadata['default_id_values'][0]

    def get_enclosed_object_metadata(self):
        """Gets the metadata"""
        return Metadata(**self._enclosed_object_metadata)

    enclosed_object_metadata = property(fget=get_enclosed_object_metadata)

    def set_enclosed_object(self, object_id):
        """Sets the Id of the object to enclose"""
        # Should add a test here to make sure the object is from this implementation
        self.my_osid_object_form._my_map['enclosedObjectId'] = str(object_id)

    def clear_enclosed_object(self):
        """Clears the Id of the enclosed object"""
        self.my_osid_object_form._my_map['enclosedObjectId'] = \
            self._enclosed_object_metadata['default_id_values'][0]

    enclosed_object = property(fset=set_enclosed_object, fdel=clear_enclosed_object)

    def get_display_name_metadata(self):
        """Overrides get_display_name_metadata of extended object"""
        metadata = dict(self.my_osid_object_form._mdata['display_name'])
        metadata.update({'read_only': True})
        return Metadata(**metadata)

    display_name_metadata = property(fget=get_display_name_metadata)

    def set_display_name(self, display_name):
        """Overrides set_display_name of extended object"""
        raise NoAccess('Display name is set in the enclosed object')

    def clear_display_name(self):
        """Overrides clear_display_name of extended object"""
        raise NoAccess('Display name is set in the enclosed object')

    display_name = property(fset=set_display_name, fdel=clear_display_name)

    def get_description_metadata(self):
        """Overrides get_description_metadata of extended object"""
        metadata = dict(self.my_osid_object_form._description_metadata)
        metadata.update({'read_only': True})
        return Metadata(**metadata)

    description_metadata = property(fget=get_description_metadata)

    def set_description(self, description):
        """Overrides set_description of extended object"""
        raise NoAccess('Description is set in the enclosed object')

    def clear_description(self):
        """Overrides clear_description of extended object"""
        raise NoAccess('Description is set in the enclosed object')

    description = property(fset=set_description, fdel=clear_description)

    def get_genus_type_metadata(self):
        """Overrides get_genus_type_metadata of extended object"""
        metadata = dict(self.my_osid_object_form._genus_type_metadata)
        metadata.update({'read_only': True})
        return Metadata(**metadata)

    genus_type_metadata = property(fget=get_genus_type_metadata)

    def set_genus_type(self, genus_type):
        """Overrides set_genus_type of extended object"""
        raise NoAccess('Genus type is detemined from the type of enclosed object')

    def clear_genus_type(self):
        """Overrides clear_genus_type of extended object"""
        raise NoAccess('Genus type is detemined from the type of enclosed object')

    genus_type = property(fset=set_genus_type, fdel=clear_genus_type)


class SimpleChildSequencingFormRecord(osid_records.OsidRecord):
    """supports simple child sequencing (like repository.objects.CompositionForm)"""

    _implemented_record_type_identifiers = [
        'simple_child_sequencing'
    ]

    def __init__(self, osid_object_form=None):
        if osid_object_form is not None:
            self.my_osid_object_form = osid_object_form
        super(SimpleChildSequencingFormRecord, self).__init__()


class SimpleChildSequencingRecord(ObjectInitRecord):
    """supports simple child sequencing (like repository.objects.Composition)"""

    _implemented_record_type_identifiers = [
        'simple_child_sequencing'
    ]
