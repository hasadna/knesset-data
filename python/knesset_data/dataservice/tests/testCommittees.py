import unittest
from knesset_data.dataservice.committees import Committee, CommitteeMeeting
from datetime import datetime


class TestCommittees(unittest.TestCase):

    def test_committee(self):
        committee = Committee.get(1)
        committees = Committee.get_page(order_by=('id', 'asc'))
        self.assertEqual(committee.name, committees[0].name)

    def test_committee_meeting(self):
        meetings = CommitteeMeeting.get(1, datetime(2016, 1, 1), datetime(2016, 1, 5))
        self.assertTrue(isinstance(meetings[0].datetime, datetime))
