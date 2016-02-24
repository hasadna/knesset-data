import unittest
from knesset_data.dataservice.committees import CommitteeMeeting
from datetime import datetime


class TestCommitteeMeetings(unittest.TestCase):

    def test_committee_meeting(self):
        meetings = CommitteeMeeting.get(1, datetime(2016, 1, 1), datetime(2016, 1, 5))
        self.assertTrue(isinstance(meetings[0].datetime, datetime))

    def test_protocol(self):
        meetings = CommitteeMeeting.get(1, datetime(2016, 2, 16), datetime(2016, 2, 17))
        meeting = meetings[0]
        with meeting.protocol as protocol:
            self.assertEqual(len(protocol.text), 33303)
