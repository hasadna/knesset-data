# -*- coding: utf-8 -*-
import unittest
from knesset_data.protocols.plenum import PlenumProtocolFile
from datetime import datetime
import os


# this function is used by test_base to test the base protocol functionality
def plenum_protocol_assertions(test_case, protocol):
    test_case.assertEqual(protocol.knesset_num_heb, 'עשרים')
    test_case.assertEqual(protocol.meeting_num_heb, 'שמונים')
    test_case.assertEqual(protocol.booklet_num_heb, 'י"א')
    test_case.assertEqual(protocol.booklet_meeting_num_heb, "פ'")
    test_case.assertEqual(protocol.date_string_heb, ('23', 'דצמבר', '2015'))
    test_case.assertEqual(protocol.time_string, ('11', '00'))
    test_case.assertEqual(protocol.datetime, datetime(2015, 12, 23, 11, 0))
    test_case.assertEqual(protocol.knesset_num, 20)
    test_case.assertEqual(protocol.booklet_num, 11)
    test_case.assertEqual(protocol.booklet_meeting_num, 80)


class TestPlenumProtocolFile(unittest.TestCase):

    def test_from_file(self):
        with PlenumProtocolFile.get_from_filename(os.path.join(os.path.dirname(__file__), '20_ptm_318579.doc')) as protocol:
            plenum_protocol_assertions(self, protocol)
