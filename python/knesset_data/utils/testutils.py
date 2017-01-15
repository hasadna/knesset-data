import tempfile
import filecmp
import os
import unittest


class TestCaseFileAssertionsMixin(object):

    def assertFileContents(self, expected_file_name, actual_content):
        with open(expected_file_name) as f:
            self.assertEqual(f.read().decode('utf-8').rstrip("\n"), actual_content.rstrip("\n"))


def data_dependant_test():
    return unittest.skip('test has hard dependency on spcecific data from Knesset, should be rewritten to be less fragile')
