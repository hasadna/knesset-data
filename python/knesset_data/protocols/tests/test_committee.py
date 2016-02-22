import unittest
from knesset_data.protocols.committee import CommitteeMeetingProtocol
import os
import filecmp
import tempfile


class TestCommitteeMeetings(unittest.TestCase):

    def test(self):
        expected_file_name = os.path.join(os.path.dirname(__file__),'20_ptv_317899.txt')
        source_doc_file_name = os.path.join(os.path.dirname(__file__),'20_ptv_317899.doc')
        with CommitteeMeetingProtocol.get_from_filename(source_doc_file_name) as protocol:
            actual_text = protocol.text
            actual_filenum, actual_file_name = tempfile.mkstemp()
            with open(actual_file_name, 'wb') as actual_file:
                actual_file.write(actual_text)
            self.assertTrue(filecmp.cmp(actual_file_name, expected_file_name))
            os.remove(actual_file_name)
