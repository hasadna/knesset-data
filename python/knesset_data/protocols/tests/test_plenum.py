# -*- coding: utf-8 -*-
import unittest
from knesset_data.protocols.plenum import PlenumProtocolFile
from datetime import datetime
import os


class TestPlenumProtocolFile(unittest.TestCase):

    def _protocol_assertions(self, protocol):
        self.assertEqual(protocol.knesset_num_heb, 'עשרים')
        self.assertEqual(protocol.meeting_num_heb, 'שמונים')
        self.assertEqual(protocol.booklet_num_heb, 'י"א')
        self.assertEqual(protocol.booklet_meeting_num_heb, "פ'")
        self.assertEqual(protocol.date_string_heb, ('23', 'דצמבר', '2015'))
        self.assertEqual(protocol.time_string, ('11', '00'))
        self.assertEqual(protocol.datetime, datetime(2015, 12, 23, 11, 0))
        self.assertEqual(protocol.knesset_num, 20)
        self.assertEqual(protocol.booklet_num, 11)
        self.assertEqual(protocol.booklet_meeting_num, 80)

    def test_from_file(self):
        with PlenumProtocolFile.get_from_filename(os.path.join(os.path.dirname(__file__), '20_ptm_318579.doc')) as protocol:
            self._protocol_assertions(protocol)

    def test_from_url(self):
        with PlenumProtocolFile.get_from_url('http://fs.knesset.gov.il//20/Plenum/20_ptm_318579.doc') as protocol:
            self._protocol_assertions(protocol)
