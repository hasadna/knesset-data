import unittest
from knesset_data.html_scrapers.votes import HtmlVote
from knesset_data.utils.testutils import data_dependant_test


class TestHtmlVote(unittest.TestCase):

    @data_dependant_test()
    def test(self):
        html_vote = HtmlVote.get_from_vote_id(24084)
        self.assertListEqual(html_vote.member_votes, [('863', 'voted for'), ('879', 'voted for'), ('953', 'voted for'), ('914', 'voted for'), ('918', 'voted for'), ('950', 'voted for'), ('922', 'voted for'), ('924', 'voted for'), ('932', 'voted for'), ('944', 'voted for'), ('230', 'voted for'), ('862', 'voted for'), ('865', 'voted for'), ('881', 'voted for'), ('818', 'voted for'), ('901', 'voted for'), ('216', 'voted for'), ('876', 'voted for'), ('915', 'voted for'), ('854', 'voted for'), ('941', 'voted for'), ('871', 'voted for')])
