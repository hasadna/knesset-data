from base import BaseKnessetDataServiceObject, KnessetDataServiceField


class Committee(BaseKnessetDataServiceObject):

    SERVICE_NAME = "CommitteeScheduleData"
    METHOD_NAME = "View_committee"
    DEFAULT_ORDER_BY_FIELD = "id"
    FIELDS = {
        'id': KnessetDataServiceField('committee_id'),
        'type_id': KnessetDataServiceField('committee_type_id'),
        'parent_id': KnessetDataServiceField('committee_parent_id'),
        'name': KnessetDataServiceField('committee_name'),
        'name_eng': KnessetDataServiceField('committee_name_eng'),
        'name_arb': KnessetDataServiceField('committee_name_arb'),
        'begin_date': KnessetDataServiceField('committee_begin_date'),
        'end_date': KnessetDataServiceField('committee_end_date'),
        'description': KnessetDataServiceField('committee_desc'),
        'description_eng': KnessetDataServiceField('committee_desc_eng'),
        'description_arb': KnessetDataServiceField('committee_desc_arb'),
        'note': KnessetDataServiceField('committee_note'),
        'note_eng': KnessetDataServiceField('committee_note_eng'),
        'portal_link': KnessetDataServiceField('committee_portal_link'),
    }
