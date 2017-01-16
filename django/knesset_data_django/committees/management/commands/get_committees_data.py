# encoding: utf-8
from django.core.management.base import NoArgsCommand
from optparse import make_option
import sys
import csv
from datetime import datetime
from knesset_data_django.committees.models import Committee
from knesset_data_django.mks.models import Member, Knesset
import logging


logger = logging.getLogger(__name__)


class Command(NoArgsCommand):
    help = "Get committees data in csv format"

    option_list = NoArgsCommand.option_list + (
        make_option('--members-attendance', dest='membersattendance', default=False, action='store_true',
                    help='get members attendance data'),
        make_option('--from-date', dest='fromdate', default='', type=str,
                    help='get data from the given date (yyyy-mm-dd)'),
        make_option('--output-file', dest='outputfile', default='', type=str,
                    help='the output file name')
    )

    def _handle_members_attendance(self, fromdate):
        committees = Committee.objects.exclude(type='plenum').exclude(hide=True)
        since_title = fromdate.strftime('%d/%m/%Y') if fromdate else u'תחילת כנסת נוכחית'
        self.csvwriter.writerow(
            [u'ועדה'.encode('utf-8'), u'ח"כ'.encode('utf-8'), (u'אחוז נוכחות מ%s' % since_title).encode('utf-8')])
        member_ids = Member.objects.filter(current_party__knesset=Knesset.objects.current_knesset()).values_list('pk',
                                                                                                                 flat=True)
        for committee in committees:
            logger.debug('processing committee %s' % committee.pk)
            members = committee.members_by_presence(ids=member_ids, from_date=fromdate)
            for member in members:
                self.csvwriter.writerow(
                    [committee.name.encode('utf-8'), member.name.encode('utf-8'), member.meetings_percentage])

    def handle_noargs(self, **options):
        if options.get('outputfile', '') == '':
            out = sys.stdout
        else:
            out = open(options['outputfile'], 'wb')
        self.csvwriter = csv.writer(out)
        if options.get('membersattendance'):
            fromdate = options.get('fromdate')
            if fromdate != '':
                fromdate = datetime.strptime(fromdate, '%Y-%m-%d').date()
            else:
                fromdate = None
            self._handle_members_attendance(fromdate)
        else:
            raise Exception('invalid args')
