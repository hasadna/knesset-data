# -*- coding: utf-8 -*-
import logging
from StringIO import StringIO
import urllib2
from pyth.plugins.rtf15.reader import Rtf15Reader
from tempfile import mkstemp
from utils import antiword, antixml
import os
from base import BaseProtocolFile


logger = logging.getLogger(__name__)


class CommitteeMeetingProtocol(BaseProtocolFile):

    # TODO: find out if the rtf protocol code is needed in some cases, currently, we don't seem to get rtf files form knesset
    # @classmethod
    # def handle_rtf_protocol(cls, file_str):
    #     # looks like this is only relevant for old meetings
    #     # this code is copied from Open-Knesset, it should work, but should keep this error until it's tested
    #     raise NotImplementedError()
    #     doc = Rtf15Reader.read(file_str)
    #     text = []
    #     attended_list = False
    #     for paragraph in doc.content:
    #         for sentence in paragraph.content:
    #             if 'bold' in sentence.properties and attended_list:
    #                 attended_list = False
    #                 text.append('')
    #             if 'מוזמנים'.decode('utf8') in sentence.content[0] and 'bold' in sentence.properties:
    #                 attended_list = True
    #             text.append(sentence.content[0])
    #     all_text = '\n'.join(text)
    #     return re.sub(r'\n:\n',r':\n',all_text)

    @property
    def text(self):
        return self.antiword_text
        # if not hasattr(self, '_cached_text'):
            # TODO: find out if rtf protocol code is needed in some cases, currently, we don't seem to get rtf files form knesset
            # url = str(self.url)
            # logger.debug('get_committee_protocol_text. url=%s' % url)
            # if url.find('html') >= 0:
            #     url = url.replace('html','rtf')
            # file_str = StringIO()
            # count = 0
            # flag = True
            # while count<10 and flag:
            #     try:
            #         file_str.write(self._get_url_contents(url))
            #         flag = False
            #     except Exception:
            #         count += 1
            # if flag:
            #     logger.error("can't open url %s. tried %d times" % (url, count))
            # if url.find(".rtf") >= 0:
            #     self._cached_text = self.handle_rtf_protocol(file_str)
        # return self._cached_text

    def parse_protocol_text(self):
        # self.create_protocol_parts(delete_existing=True)
        # self.find_attending_members(mks, mk_names)
        pass