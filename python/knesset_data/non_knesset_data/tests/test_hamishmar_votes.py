import unittest
from knesset_data.non_knesset_data.hamishmar_votes import HamishmarVote
import os
from datetime import datetime


class TestHamishmarVotes(unittest.TestCase):

    def test(self):
        with open(os.path.join(os.path.dirname(__file__), 'hamishmar_votes_data.csv'), 'r') as f:
            votes = HamishmarVote.get_from_csv(f)
            vote = votes[0]
            self.assertEqual(vote.id, 155)
            self.assertEqual(vote.date, datetime(2015, 12, 23))
            self.assertEqual(vote.protocol_url, 'http://fs.knesset.gov.il//20/Plenum/20_ptm_318579.doc')
            self.assertEqual(len(vote.voted_for_member_names), 53)
            self.assertEqual(len(vote.voted_against_member_names), 54)
            self.assertEqual(len(vote.voted_for_party_names), 5)
            self.assertEqual(len(vote.voted_against_party_names), 5),
            self.assertEqual(vote.voted_for_count, '53')
            self.assertEqual(vote.voted_against_count, '54')
            self.assertEqual(vote.vote_result, '-1')
