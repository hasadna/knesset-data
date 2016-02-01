from base import BaseKnessetDataServiceObject, KnessetDataServiceSimpleField, KnessetDataServiceDateTimeField, KnessetDataServiceStrptimeField


class Committee(BaseKnessetDataServiceObject):

    SERVICE_NAME = "CommitteeScheduleData"
    METHOD_NAME = "View_committee"
    DEFAULT_ORDER_BY_FIELD = "id"
    
    id = KnessetDataServiceSimpleField('committee_id')
    type_id = KnessetDataServiceSimpleField('committee_type_id')
    parent_id = KnessetDataServiceSimpleField('committee_parent_id')
    name = KnessetDataServiceSimpleField('committee_name')
    name_eng = KnessetDataServiceSimpleField('committee_name_eng')
    name_arb = KnessetDataServiceSimpleField('committee_name_arb')
    begin_date = KnessetDataServiceSimpleField('committee_begin_date')
    end_date = KnessetDataServiceSimpleField('committee_end_date')
    description = KnessetDataServiceSimpleField('committee_desc')
    description_eng = KnessetDataServiceSimpleField('committee_desc_eng')
    description_arb = KnessetDataServiceSimpleField('committee_desc_arb')
    note = KnessetDataServiceSimpleField('committee_note')
    note_eng = KnessetDataServiceSimpleField('committee_note_eng')
    portal_link = KnessetDataServiceSimpleField('committee_portal_link')


class CommitteeMeeting(BaseKnessetDataServiceObject):

    SERVICE_NAME = "CommitteeScheduleData"
    METHOD_NAME = "View_protocols"
    DEFAULT_ORDER_BY_FIELD = "date"

    id = KnessetDataServiceSimpleField('Protocol_id')
    committee_id = KnessetDataServiceSimpleField('Committee_id')
    date = KnessetDataServiceSimpleField('Protocol_date')
    time = KnessetDataServiceStrptimeField('Protocol_time')
    datetime = KnessetDataServiceDateTimeField('date', 'time')
    agendum1 = KnessetDataServiceSimpleField('AGENDUM1')
    agendum2 = KnessetDataServiceSimpleField('AGENDUM2')
    agendum3 = KnessetDataServiceSimpleField('AGENDUM3')
    agendum4 = KnessetDataServiceSimpleField('AGENDUM4')
    agendum5 = KnessetDataServiceSimpleField('AGENDUM5')
    agendum6 = KnessetDataServiceSimpleField('AGENDUM6')
    agendum7 = KnessetDataServiceSimpleField('AGENDUM7')
    agendum8 = KnessetDataServiceSimpleField('AGENDUM8')
    nochechim = KnessetDataServiceSimpleField('NOCHECHIM')
    muzmanim = KnessetDataServiceSimpleField('MUZMANIM')
    yoetz = KnessetDataServiceSimpleField('YOETZ')
    menahel = KnessetDataServiceSimpleField('MENAHEL')
    link = KnessetDataServiceSimpleField('Protocol_link')
