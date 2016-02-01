from base import BaseKnessetDataServiceObject, KnessetDataServiceSimpleField, KnessetDataServiceStrptimeField, KnessetDataServiceDateTimeField
import datetime


class VoteTimeField(KnessetDataServiceStrptimeField):

    def get_value(self, entry, obj=None):
        str = super(KnessetDataServiceStrptimeField, self).get_value(entry)
        str = "00:00" if str is None else str  # see https://github.com/hasadna/knesset-data/issues/2
        return datetime.datetime.strptime(str, self._strptime_format)


class Vote(BaseKnessetDataServiceObject):

    SERVICE_NAME = "VotesData"
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
