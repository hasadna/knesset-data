from urllib2 import urlopen
import contextlib
from tempfile import mkstemp
import os
from utils import antiword, antixml


class BaseProtocolFile(object):

    def __init__(self, file):
        self._file_type, self._file_data = file

    def _get_file_from_url(self, url):
        # allows to modify the url opening in extending classes
        return urlopen(url)

    @property
    def file(self):
        if not hasattr(self, '_cached_file'):
            if self._file_type == 'url':
                self._cached_file = self._get_file_from_url(self._file_data)
            elif self._file_type == 'filename':
                self._cached_file = open(self._file_data)
            elif self._file_type == 'file':
                self._cached_file = self._file_data
            elif self._file_type == 'data':
                self._cached_file = open(self.file_name)
            else:
                raise NotImplementedError('file type %s is not supported'%self._file_type)
        return self._cached_file

    @property
    def file_name(self):
        if not hasattr(self, '_cached_file_name'):
            if self._file_type == 'filename':
                self._cached_file_name = self._file_data
            else:
                fid, fname = mkstemp()
                f = open(fname, 'wb')
                f.write(self.file_contents)
                f.close()
                self._cached_file_name = fname
        return self._cached_file_name

    @property
    def file_contents(self):
        if not hasattr(self, '_cached_file_contents'):
            if self._file_type == 'data':
                return self._file_data
            else:
                self._cached_file_contents = self.file.read()
        return self._cached_file_contents

    @property
    def antiword_xml(self):
        if not hasattr(self, '_cached_antiword_xml'):
            self._cached_antiword_xml = antiword(self.file_name)
        return self._cached_antiword_xml

    @property
    def antiword_text(self):
        if not hasattr(self, '_cached_antiword_text'):
            self._cached_antiword_text = antixml(self.antiword_xml)
        return self._cached_antiword_text

    def _close(self):
        if hasattr(self, '_cached_file') and self._file_type != 'file': self._cached_file.close()
        if hasattr(self, '_cached_file_name') and self._file_type != 'filename': os.remove(self._cached_file_name)

    @classmethod
    @contextlib.contextmanager
    def get_from_url(cls, url):
        obj = cls(('url', url))
        yield obj
        obj._close()

    @classmethod
    @contextlib.contextmanager
    def get_from_file(cls, file):
        obj = cls(('file', file))
        yield obj
        obj._close()

    @classmethod
    @contextlib.contextmanager
    def get_from_filename(cls, filename):
        obj = cls(('filename', filename))
        yield obj
        obj._close()

    @classmethod
    @contextlib.contextmanager
    def get_from_data(cls, data):
        obj = cls(('data', data))
        yield obj
        obj._close()
