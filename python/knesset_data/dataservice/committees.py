# -*- coding: utf-8 -*-
from base import (
    BaseKnessetDataServiceCollectionObject, BaseKnessetDataServiceFunctionObject,
    KnessetDataServiceSimpleField, KnessetDataServiceDateTimeField, KnessetDataServiceStrptimeField,
)
import logging
from cStringIO import StringIO
import urllib2
from tempfile import mkstemp
import os
import re
import subprocess
from pyth.plugins.rtf15.reader import Rtf15Reader
from knesset_data.utils.protocol_files import antiword, antixml


logger = logging.getLogger('knesset_data.dataservice.committees')


class Committee(BaseKnessetDataServiceCollectionObject):

    SERVICE_NAME = "committees"
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

    @classmethod
    def get_all_active_committees(cls):
        url = cls._get_url_base()+'?$filter=committee_portal_link%20ne%20null%20and%20committee_end_date%20eq%20null'
        soup = cls._get_soup(url)
        return [cls(cls._parse_entry(entry)) for entry in soup.feed.find_all('entry')]


class CommitteeMeeting(BaseKnessetDataServiceFunctionObject):

    SERVICE_NAME = "committees"
    METHOD_NAME = "CommitteeAgendaSearch"

    # the primary key of committee meetings
    id = KnessetDataServiceSimpleField('Committee_Agenda_id')

    # id of the committee (linked to Committee object)
    committee_id = KnessetDataServiceSimpleField('Committee_Agenda_committee_id')

    # date/time when the meeting started
    datetime = KnessetDataServiceSimpleField('committee_agenda_date')

    # title of the meeting
    title = KnessetDataServiceSimpleField('title')

    # url to download the protocol
    url = KnessetDataServiceSimpleField('url')

    # this seems like a shorter name of the place where meeting took place
    location = KnessetDataServiceSimpleField('committee_location')

    # this looks like a longer field with the specific details of where the meeting took place
    place = KnessetDataServiceSimpleField('Committee_Agenda_place')

    # date/time when the meeting ended
    meeting_stop = KnessetDataServiceSimpleField('meeting_stop')

    ### following fields seem less interesting ###
    session_content = KnessetDataServiceSimpleField('committee_agenda_session_content')
    agenda_canceled = KnessetDataServiceSimpleField('Committee_Agenda_canceled')
    agenda_sub = KnessetDataServiceSimpleField('Committee_agenda_sub')
    agenda_associated = KnessetDataServiceSimpleField('Committee_agenda_associated')
    agenda_associated_id = KnessetDataServiceSimpleField('Committee_agenda_associated_id')
    agenda_special = KnessetDataServiceSimpleField('Committee_agenda_special')
    agenda_invited1 = KnessetDataServiceSimpleField('Committee_agenda_invited1')
    agenda_invite = KnessetDataServiceSimpleField('sd2committee_agenda_invite')
    note = KnessetDataServiceSimpleField('Committee_agenda_note')
    start_datetime = KnessetDataServiceSimpleField('StartDateTime')
    topid_id = KnessetDataServiceSimpleField('Topic_ID')
    creation_date = KnessetDataServiceSimpleField('Date_Creation')
    streaming_url = KnessetDataServiceSimpleField('streaming_url')
    meeting_start = KnessetDataServiceSimpleField('meeting_start')
    is_paused = KnessetDataServiceSimpleField('meeting_is_paused')
    date_order = KnessetDataServiceSimpleField('committee_date_order')
    date = KnessetDataServiceSimpleField('committee_date')
    day = KnessetDataServiceSimpleField('committee_day')
    month = KnessetDataServiceSimpleField('committee_month')
    material_id = KnessetDataServiceSimpleField('material_id')
    material_committee_id = KnessetDataServiceSimpleField('material_comittee_id')
    material_expiration_date = KnessetDataServiceSimpleField('material_expiration_date')
    material_hour = KnessetDataServiceSimpleField('committee_material_hour')
    old_url = KnessetDataServiceSimpleField('OldUrl')
    background_page_link = KnessetDataServiceSimpleField('CommitteeBackgroundPageLink')
    agenda_invited = KnessetDataServiceSimpleField('Committee_agenda_invited')

    @classmethod
    def handle_doc_protocol(cls, file_str):
        """
        if you want to work on this function you should check out tests.committees.test_protocols
        and `python bin/handle_doc_protocol.py`
        """
        fid, fname = mkstemp()
        f = open(fname, 'wb')
        file_str.seek(0)
        f.write(file_str.read())
        f.close()
        x = antiword(fname)
        os.remove(fname)
        return antixml(x)

    @classmethod
    def handle_rtf_protocol(cls, file_str):
        raise NotImplementedError()
        doc = Rtf15Reader.read(file_str)
        text = []
        attended_list = False
        for paragraph in doc.content:
            for sentence in paragraph.content:
                if 'bold' in sentence.properties and attended_list:
                    attended_list = False
                    text.append('')
                if 'מוזמנים'.decode('utf8') in sentence.content[0] and 'bold' in sentence.properties:
                    attended_list = True
                text.append(sentence.content[0])
        all_text = '\n'.join(text)
        return re.sub(r'\n:\n',r':\n',all_text)

    def get_protocol_text(self):
        url = str(self.url)
        logger.debug('get_committee_protocol_text. url=%s' % url)
        if url.find('html') >= 0:
            url = url.replace('html','rtf')
        file_str = StringIO()
        count = 0
        flag = True
        while count<10 and flag:
            try:
                file_str.write(urllib2.urlopen(url).read())
                flag = False
            except Exception:
                count += 1
        if flag:
            logger.error("can't open url %s. tried %d times" % (url, count))

        if url.find(".rtf") >= 0:
            return self.handle_rtf_protocol(file_str)
        if url.find(".doc") >= 0:
            return self.handle_doc_protocol(file_str)

    def parse_protocol_text(self):
        # self.create_protocol_parts(delete_existing=True)
        # self.find_attending_members(mks, mk_names)
        pass

    @classmethod
    def get(cls, committee_id, from_date, to_date=None):
        """
        # example usage:
        >>> from datetime import datetime
        # get all meetings of committee 1 from Jan 01, 2016
        >>> CommitteeMeeting.get(1, datetime(2016, 1, 1))
        # get all meetings of committee 2 from Feb 01, 2015 to Feb 20, 2015
        >>> CommitteeMeeting.get(2, datetime(2015, 2, 1), datetime(2015, 2, 20))
        """
        params = {
            "CommitteeId": "'%s'"%committee_id,
            "FromDate": "'%sT00:00:00'"%from_date.strftime('%Y-%m-%d')
        }
        if to_date:
            params["ToDate"] = "'%sT00:00:00'"%to_date.strftime('%Y-%m-%d')
        return super(CommitteeMeeting, cls).get(params)
