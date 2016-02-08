import unittest
from knesset_data.dataservice.committees import CommitteeMeeting
from datetime import datetime
import os
import filecmp
import tempfile

class TestCommitteeMeetings(unittest.TestCase):

    def test_handle_doc(self):
        # if you want to work on the handle_doc_protocol function, check out `python bin/handle_doc_protocol.py`
        expected_file_name = os.path.join(os.path.dirname(__file__),'20_ptv_317899.txt')
        source_doc_file_name = os.path.join(os.path.dirname(__file__),'20_ptv_317899.doc')
        with open(source_doc_file_name) as source_doc_file:
            actual_text = CommitteeMeeting.handle_doc_protocol(source_doc_file)
            actual_filenum, actual_file_name = tempfile.mkstemp()
            with open(actual_file_name, 'wb') as actual_file:
                actual_file.write(actual_text)
            self.assertTrue(filecmp.cmp(actual_file_name, expected_file_name))
            os.remove(actual_file_name)
