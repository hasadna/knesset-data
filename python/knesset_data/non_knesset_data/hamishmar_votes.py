import csv
from datetime import datetime


class HamishmarVote(object):

    def __init__(self, data):
        self.data = data
        # 'Law_ID'
        # 'Con_mishmar_parties'
        # 'Pro_mishmar'
        # 'Pro_mishmar_parties'
        # 'Data_Vote'
        # None
        # '\xef\xbb\xbf"ID"'
        # 'Vote_stage'
        # 'Vote_system_name'
        # 'Vote_date'
        # 'Con Parties'
        # 'Con_mishmar'
        # 'Pro_count'
        # 'Con'
        # 'Agenda_status'
        # 'Oknesset_link'
        # 'Pro_parties'
        # 'Pro'
        # 'Con_count'
        # 'Result'
        # 'Name_comment'
        # 'Hamishmar decision'

    @property
    def id(self):
        return int(self.data.get('ID', self.data.get('\xef\xbb\xbf"ID"')))

    @property
    def date(self):
        date = self.data.get('Vote_date')
        return datetime.strptime(date, '%d/%m/%Y')

    @property
    def protocol_url(self):
        """
        returns a link to the protocol document where this vote appears
        e.g. http://fs.knesset.gov.il//20/Plenum/20_ptm_318579.doc
        """
        return self.data.get('Oknesset_link')

    @property
    def voted_for_member_names(self):
        return self.data.get('Pro').split("\n")

    @property
    def voted_against_member_names(self):
        return self.data.get('Con').split("\n")

    @property
    def voted_for_party_names(self):
        return self.data.get('Pro_parties').split("\n")

    @property
    def voted_against_party_names(self):
        return self.data.get('Con Parties').split("\n")

    @property
    def voted_for_count(self):
        return self.data.get('Pro_count')

    @property
    def voted_against_count(self):
        return self.data.get('Con_count')

    @property
    def vote_result(self):
        # -1 = against
        # 1 = for
        return self.data.get('Result')

    @classmethod
    def get_from_csv(cls, f):
        return [cls(line) for line in csv.DictReader(f)]
