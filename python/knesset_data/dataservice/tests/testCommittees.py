import unittest
from knesset_data.dataservice.committees import Committee


class TestCommittees(unittest.TestCase):

    def test(self):
        committee = Committee.get(1)
        committees = Committee.get_page(order_by=('id', 'asc'))
        self.assertEqual(committee.name, committees[0].name)
