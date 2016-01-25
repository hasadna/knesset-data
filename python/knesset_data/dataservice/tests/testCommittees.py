import unittest
from knesset_data.dataservice.committees import Committee, CommitteeMeeting
from datetime import datetime


class TestCommittees(unittest.TestCase):

    def test_committee(self):
        committee = Committee.get(1)
        committees = Committee.get_page(order_by=('id', 'asc'))
        self.assertEqual(committee.name, committees[0].name)

    def test_committee_meeting(self):
        meeting = CommitteeMeeting.get(53)
        meetings = CommitteeMeeting.get_page()
        self.assertTrue(isinstance(meeting.datetime, datetime))
        self.assertTrue(isinstance(meetings[5].datetime, datetime))
