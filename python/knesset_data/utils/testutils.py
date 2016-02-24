import tempfile
import filecmp
import os


class TestCaseFileAssertionsMixin(object):

    def assertFileContents(self, expected_file_name, actual_content):
        with open(expected_file_name) as f:
            self.assertEqual(f.read().decode('utf-8').rstrip("\n"), actual_content.rstrip("\n"))
