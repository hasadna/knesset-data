# -*- coding: utf-8 -*-
from urllib2 import urlopen
from tempfile import mkstemp
from datetime import datetime
from hebrew_numbers import gematria_to_int
from utils import antiword, antixml
import re
from base import BaseProtocolFile


class PlenumProtocolFile(BaseProtocolFile):

    @property
    def header_text(self):
        if not hasattr(self, '_cached_header_text'):
            self._cached_header_text = self.antiword_text[:1000].replace("\n", "NL")
        return self._cached_header_text

    @property
    def meeting_num_heb(self):
        match = re.search(r'הישיבה ה(.*) של הכנסת', self.header_text)
        return match.groups()[0].strip() if match else None

    @property
    def knesset_num_heb(self):
        match = re.search(r'של הכנסת ה(.+?(?=NL))', self.header_text)
        return match.groups()[0].strip() if match else None

    @property
    def knesset_num(self):
        # TODO: write a proper algorythm (maybe add it to https://github.com/OriHoch/python-hebrew-numbers)
        return {
            'עשרים': 20,
            'עשרים ואחת': 21,
            'עשרים ושתיים': 22
        }[self.knesset_num_heb]

    @property
    def booklet_num(self):
        return gematria_to_int(self.booklet_num_heb.decode('utf-8'))

    @property
    def booklet_num_heb(self):
        match = re.search(r'חוברת (.+?(?=NL))', self.header_text)
        return match.groups()[0].strip() if match else None

    @property
    def booklet_meeting_num(self):
        return gematria_to_int(self.booklet_meeting_num_heb.decode('utf-8'))

    @property
    def booklet_meeting_num_heb(self):
        match = re.search(r'ישיבה (.+?(?=NL))', self.header_text)
        return match.groups()[0].strip() if match else None

    @property
    def day_heb(self):
        match = re.search(r'יום ([קראטוןםפףךלחיעכגדשזסבהנמצתץ]*)', self.header_text)
        return match.groups()[0].strip() if match else None

    @property
    def date_string_heb(self):
        match = re.search(r'\(([0-9]+) ב([קראטוןםפףךלחיעכגדשזסבהנמצתץ]+) ([0-9]+)\)', self.header_text)
        day, month_name_heb, year = match.groups()[0].strip(), match.groups()[1].strip(), match.groups()[2].strip()
        return day, month_name_heb, year

    @property
    def time_string(self):
        match = re.search(r'שעה ([0-9]+):([0-9]+)(.+?(?=NL))', self.header_text)
        hours, minutes = match.groups()[0].strip(), match.groups()[1].strip()
        return hours, minutes

    @property
    def datetime(self):
        day, month_name_heb, year = self.date_string_heb
        hours, minutes = self.time_string
        months = ['ינואר', 'פברואר', 'מרץ', 'אפריל', 'מאי', 'יוני', 'יולי', 'אוגוסט', 'ספטמבר', 'אוקטובר', 'נובמבר', 'דצמבר']
        month = months.index(month_name_heb)+1
        return datetime(int(year), month, int(day), int(hours), int(minutes))
