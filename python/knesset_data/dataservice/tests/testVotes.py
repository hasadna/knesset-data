import unittest
from knesset_data.dataservice.votes import Vote
from datetime import datetime


class TestVotes(unittest.TestCase):

    def test(self):
        res = Vote.get_page()
        vote = res[5]
        self.assertTrue(isinstance(vote.datetime, datetime))
