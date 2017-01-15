import unittest
from knesset_data.dataservice.votes import Vote
from datetime import datetime
from knesset_data.utils.testutils import data_dependant_test

class TestVotes(unittest.TestCase):

    @data_dependant_test()
    def test(self):
        res = Vote.get_page()
        vote = res[5]
        self.assertTrue(isinstance(vote.datetime, datetime))
