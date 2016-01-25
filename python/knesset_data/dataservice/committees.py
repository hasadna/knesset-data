from base import BaseKnessetDataServiceObject, KnessetDataServiceSimpleField


class Committee(BaseKnessetDataServiceObject):

    SERVICE_NAME = "CommitteeScheduleData"
    METHOD_NAME = "View_committee"
    DEFAULT_ORDER_BY_FIELD = "id"
    FIELDS = {
        'id': KnessetDataServiceSimpleField('committee_id'),
        'type_id': KnessetDataServiceSimpleField('committee_type_id'),
        'parent_id': KnessetDataServiceSimpleField('committee_parent_id'),
        'name': KnessetDataServiceSimpleField('committee_name'),
        'name_eng': KnessetDataServiceSimpleField('committee_name_eng'),
        'name_arb': KnessetDataServiceSimpleField('committee_name_arb'),
        'begin_date': KnessetDataServiceSimpleField('committee_begin_date'),
        'end_date': KnessetDataServiceSimpleField('committee_end_date'),
        'description': KnessetDataServiceSimpleField('committee_desc'),
        'description_eng': KnessetDataServiceSimpleField('committee_desc_eng'),
        'description_arb': KnessetDataServiceSimpleField('committee_desc_arb'),
        'note': KnessetDataServiceSimpleField('committee_note'),
        'note_eng': KnessetDataServiceSimpleField('committee_note_eng'),
        'portal_link': KnessetDataServiceSimpleField('committee_portal_link'),
    }
