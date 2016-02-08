import unittest
from knesset_data.dataservice.committees import CommitteeMeeting
from datetime import datetime


class TestCommitteeMeetings(unittest.TestCase):

    def test_committee_meeting(self):
        meetings = CommitteeMeeting.get(1, datetime(2016, 1, 1), datetime(2016, 1, 5))
        self.assertTrue(isinstance(meetings[0].datetime, datetime))
