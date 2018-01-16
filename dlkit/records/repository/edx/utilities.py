import re
import tarfile

from datetime import datetime

from io import BytesIO

from dlkit.runtime.errors import IllegalState


def clean_str(input_):
    """
    Remove all non-words from a string
    """
    output = re.sub(r'[^\w]', '_', input_)
    return output


def get_byte_stream_size(stream):
    size = int(stream.tell())
    if size == 0:
        size = len(stream.read())
    return size


def get_current_time_in_secs():
    # For Python 2.7+
    # time = int((datetime.utcnow() - datetime(1970,1,1)).total_seconds())
    # For older versions:
    # https://bitbucket.org/wnielson/django-chronograph/issue/21/timedeltatotal_seconds-requires-python-27
    td = datetime.utcnow() - datetime(1970, 1, 1)
    time = td.seconds + td.days * 24 * 3600
    return time


def remove_redundant_drafts(path):
    """
    Hack to keep only one "/drafts/" in the filepath
    """
    return path.replace('drafts/drafts', 'drafts')


def remove_trailing_slash(path):
    if path[-1] == '/':
        return path[:-1]
    else:
        return path


def slugify(string):
    try:
        from django.utils.text import slugify
        return slugify(string)
    except ImportError:
        string = re.sub('[^\w\s-]', '', string.lower())
        return re.sub('[-\s]+', '-', string)


class EdXUtilitiesMixin(object):
    def get_unique_name(self, tarball, expected_name, tag, path):
        orig_name = expected_name
        name_is_unique = False
        my_xml_path = '{0}{1}/{2}.xml'.format(path,
                                              tag,
                                              expected_name)
        counter = 1
        while not name_is_unique:
            if my_xml_path not in tarball.getnames():
                name_is_unique = True
            else:
                expected_name = '{0}-{1}'.format(orig_name,
                                                 str(counter))
                my_xml_path = '{0}{1}/{2}.xml'.format(path,
                                                      tag,
                                                      expected_name)
                counter += 1
        return expected_name

    @property
    def url(self):
        return slugify(self.my_osid_object.display_name.text)

    def write_to_tarfile(self, tarball, path, soup=None, fileobj=None, prettify=True):
        fixed_path = remove_redundant_drafts(path)
        f = tarfile.TarInfo(name=remove_trailing_slash(fixed_path))
        f.mtime = get_current_time_in_secs()
        f.mode = 0o755
        f.uname = 'MIT_ODL'
        f.gname = 'staff'

        if soup is None and fileobj is None:
            f.type = tarfile.DIRTYPE
            tarball.addfile(f)
        elif soup is not None and fileobj is not None:
            raise IllegalState('cannot provide both soup and fileobj')
        elif soup is not None:
            if prettify:
                try:
                    if soup.find_all(group_id_to_child=True):
                        stream = BytesIO(soup.prettify(formatter=None).encode('utf-8'))
                    else:
                        stream = BytesIO(soup.prettify().encode('utf-8'))
                except AttributeError:
                    stream = BytesIO(soup.read())
            else:
                try:
                    stream = BytesIO(str(soup))
                except (UnicodeDecodeError, TypeError):
                    stream = BytesIO(soup.encode('utf-8'))
            f.size = get_byte_stream_size(stream)
            stream.seek(0)
            tarball.addfile(f, stream)
        else:
            tarball.add(fileobj.name, arcname=fixed_path)
