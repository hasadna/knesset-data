import unittest
from datetime import datetime
from knesset_data.dataservice.committees import CommitteeMeeting
from knesset_data.utils.testutils import data_dependant_test


class TestCommitteeMeetings(unittest.TestCase):

    def _get_meetings(self, committee_id, datetime_from, datetime_to):
        # the knesset dataservice allows to get meetings only using a function with these parameters
        # see https://github.com/hasadna/knesset-data/issues/25
        return CommitteeMeeting.get(committee_id, datetime_from, datetime_to)

    @data_dependant_test()
    def test_committee_meeting(self):
        meetings = self._get_meetings(1, datetime(2016, 1, 1), datetime(2016, 1, 5))
        self.assertTrue(isinstance(meetings[0].datetime, datetime))
        # for more details about the available data see knesset_data/dataservice/committees.py
        # TODO: add assertion here for each relevant field

    @data_dependant_test()
    def test_protocol(self):
        meetings = self._get_meetings(1, datetime(2016, 2, 16), datetime(2016, 2, 17))
        meeting = meetings[0]
        # because parsing the protocol requires heavy IO and processing - we provide it as a generator
        # also, we need to ensure temp files are deleted
        with meeting.protocol as protocol:
            # see knesset_data/protocols/tests/test_committee.py for example of getting more data from the protocol
            self.assertEqual(len(protocol.text), 33303)
