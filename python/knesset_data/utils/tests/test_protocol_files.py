# -*- coding: utf-8 -*-
import unittest
from knesset_data.utils.protocol_files import PlenumProtocolFile
from datetime import datetime

class TestProtocolFiles(unittest.TestCase):

    def test(self):
        url = 'http://fs.knesset.gov.il//20/Plenum/20_ptm_318579.doc'
        file = PlenumProtocolFile.get_from_url(url)
        self.assertEqual(file.knesset_num_heb, 'עשרים')
        self.assertEqual(file.meeting_num_heb, 'שמונים')
        self.assertEqual(file.booklet_num_heb, 'י"א')
        self.assertEqual(file.booklet_meeting_num_heb, "פ'")
        self.assertEqual(file.date_string_heb, ('23', 'דצמבר', '2015'))
        self.assertEqual(file.time_string, ('11', '00'))
        self.assertEqual(file.datetime, datetime(2015, 12, 23, 11, 0))
        self.assertEqual(file.knesset_num, 20)
        self.assertEqual(file.booklet_num, 11)
        self.assertEqual(file.booklet_meeting_num, 80)
