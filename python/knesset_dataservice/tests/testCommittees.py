import unittest
from knesset_dataservice.committees import Committee


class TestCommittees(unittest.TestCase):

    def test(self):
        committee = Committee.get(1)
        committees = Committee.get_page(order_by=('id', 'asc'))
        self.assertEqual(committee.name, committees[0].name)
        all_committees = Committee.get_pages()
        print [c.id for c in all_committees]