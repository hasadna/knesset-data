from base import BaseKnessetDataServiceCollectionObject, KnessetDataServiceSimpleField, KnessetDataServiceStrptimeField, KnessetDataServiceDateTimeField
import datetime


class VoteTimeField(KnessetDataServiceStrptimeField):

    def get_value(self, entry, obj=None):
        str = super(KnessetDataServiceStrptimeField, self).get_value(entry)
        str = "00:00" if str is None else str  # see https://github.com/hasadna/knesset-data/issues/2
        return datetime.datetime.strptime(str, self._strptime_format)


class VoteMemberIdField(KnessetDataServiceSimpleField):

    def get_value(self, entry):
        str = super(VoteMemberIdField, self).get_value(entry)
        return int(str)


class VoteMember(BaseKnessetDataServiceCollectionObject):

    SERVICE_NAME = "votes"
    METHOD_NAME = "vote_rslts_kmmbr_shadow"
    DEFAULT_ORDER_BY_FIELD = "vote_id"

    # linked to Vote.id
    vote_id = KnessetDataServiceSimpleField('vote_id')
    # the mk id
    member_id = VoteMemberIdField('kmmbr_id')
    # numerical id linked to vote_result_type
    # normally you will use vote_result_code property instead
    vote_result = KnessetDataServiceSimpleField('vote_result')
    knesset_num = KnessetDataServiceSimpleField('knesset_num')
    # not sure what these fields do..
    reason = KnessetDataServiceSimpleField('reason')
    modifier = KnessetDataServiceSimpleField('modifier')
    remark = KnessetDataServiceSimpleField('remark')

    @property
    def vote_result_code(self):
        # this is based on vote service, vote_result_type method
        # I assume / hope it won't change..
        return {
            0: 'cancelled',
            1: 'voted for',
            2: 'voted against',
            3: 'abstain',
            4: 'did not vote',
        }[self.vote_result]

    @classmethod
    def get_by_vote_id(cls, vote_id):
        start_url = cls._get_url_base()+'?$filter=vote_id%%20eq%%20%s'%vote_id
        return cls._get_all_pages(start_url)


class Vote(BaseKnessetDataServiceCollectionObject):

    SERVICE_NAME = "votes"
    METHOD_NAME = "View_vote_rslts_hdr_Approved"
    DEFAULT_ORDER_BY_FIELD = "date"

    id = KnessetDataServiceSimpleField('vote_id')
    knesset_num = KnessetDataServiceSimpleField('knesset_num')
    session_id = KnessetDataServiceSimpleField('session_id')
    sess_item_nbr = KnessetDataServiceSimpleField('sess_item_nbr')
    sess_item_id = KnessetDataServiceSimpleField('sess_item_id')
    sess_item_dscr = KnessetDataServiceSimpleField('sess_item_dscr')
    item_id = KnessetDataServiceSimpleField('vote_item_id')
    item_dscr = KnessetDataServiceSimpleField('vote_item_dscr')
    date = KnessetDataServiceSimpleField('vote_date')
    time = VoteTimeField('vote_time')
    datetime = KnessetDataServiceDateTimeField('date', 'time')
    is_elctrnc_vote = KnessetDataServiceSimpleField('is_elctrnc_vote')
    type = KnessetDataServiceSimpleField('vote_type')
    is_accepted = KnessetDataServiceSimpleField('is_accepted')
    total_for = KnessetDataServiceSimpleField('total_for')
    total_against = KnessetDataServiceSimpleField('total_against')
    total_abstain = KnessetDataServiceSimpleField('total_abstain')
    stat = KnessetDataServiceSimpleField('vote_stat')
    session_num = KnessetDataServiceSimpleField('session_num')
    nbr_in_sess = KnessetDataServiceSimpleField('vote_nbr_in_sess')
    reason = KnessetDataServiceSimpleField('reason')
    modifier = KnessetDataServiceSimpleField('modifier')
    remark = KnessetDataServiceSimpleField('remark')
