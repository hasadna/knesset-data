# -*- coding: utf-8 -*-
import unittest
from knesset_data.protocols.plenum import PlenumProtocolFile
from datetime import datetime
import os
from test_plenum import plenum_protocol_assertions


class TestBaseProtocolFile(unittest.TestCase):

    def test_from_filename(self):
        with PlenumProtocolFile.get_from_filename(os.path.join(os.path.dirname(__file__), '20_ptm_318579.doc')) as protocol:
            plenum_protocol_assertions(self, protocol)

    def test_from_url(self):
        with PlenumProtocolFile.get_from_url('http://fs.knesset.gov.il/20/Plenum/20_ptm_318579.doc') as protocol:
            plenum_protocol_assertions(self, protocol)

    def test_from_content(self):
        with open(os.path.join(os.path.dirname(__file__), '20_ptm_318579.doc')) as f:
            with PlenumProtocolFile.get_from_data(f.read()) as protocol:
                plenum_protocol_assertions(self, protocol)

    def test_from_file(self):
        with open(os.path.join(os.path.dirname(__file__), '20_ptm_318579.doc')) as f:
            with PlenumProtocolFile.get_from_file(f) as protocol:
                plenum_protocol_assertions(self, protocol)
