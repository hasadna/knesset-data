import unittest
from knesset_data.dataservice.votes import Vote, VoteMember
from knesset_data.utils.testutils import data_dependant_test


class TestVotes(unittest.TestCase):

    @data_dependant_test()
    def test(self):
        vote = Vote.get(94)
        vote_members = VoteMember.get_by_vote_id(vote.id)
        total_for, total_against, total_abstain = 0, 0, 0
        for vote_member in vote_members:
            if vote_member.vote_result_code == 'voted for':
                total_for += 1
            elif vote_member.vote_result_code == 'voted against':
                total_against += 1
            elif vote_member.vote_result_code == 'abstain':
                total_abstain += 1
        self.assertEqual(vote.total_for, total_for)
        self.assertEqual(vote.total_against, total_against)
        self.assertEqual(vote.total_abstain, total_abstain)
        self.assertTrue(isinstance(vote_member.member_id, int))
