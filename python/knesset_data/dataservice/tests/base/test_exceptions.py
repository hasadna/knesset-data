import unittest
from datetime import datetime
from knesset_data.dataservice.committees import Committee, CommitteeMeeting
from knesset_data.dataservice.exceptions import KnessetDataServiceRequestException
from knesset_data.utils.testutils import data_dependant_test


class CommitteeWithVeryShortTimeoutAndInvalidService(Committee):
    DEFAULT_REQUEST_TIMEOUT_SECONDS = 1
    METHOD_NAME = "Invalid Method Name"


class CommitteeMeetingWithVeryShortTimeoutAndInvalidService(CommitteeMeeting):
    DEFAULT_REQUEST_TIMEOUT_SECONDS = 1
    METHOD_NAME = "FOOBARBAZBAX"


class TestDataServiceRequestExceptions(unittest.TestCase):

    @data_dependant_test()
    def test_committee(self):
        exception = None
        try:
            CommitteeWithVeryShortTimeoutAndInvalidService.get(1)
        except KnessetDataServiceRequestException as e:
            exception = e
        self.assertIsInstance(exception, KnessetDataServiceRequestException)
        self.assertListEqual([
            exception.knesset_data_method_name,
            exception.knesset_data_service_name,
            exception.url,
            str(exception.message)
        ], [
            'Invalid Method Name',
            'committees',
            'http://online.knesset.gov.il/WsinternetSps/KnessetDataService/CommitteeScheduleData.svc/Invalid%20Method%20Name(1)',
            "('Connection aborted.', error(104, 'Connection reset by peer'))",
        ])

    @data_dependant_test()
    def test_committee_meeting(self):
        exception = None
        try:
            CommitteeMeetingWithVeryShortTimeoutAndInvalidService.get(1, datetime(2016, 1, 1))
        except KnessetDataServiceRequestException as e:
            exception = e
        self.assertIsInstance(exception, KnessetDataServiceRequestException)
        self.assertListEqual([
            exception.knesset_data_method_name,
            exception.knesset_data_service_name,
            exception.url,
            str(exception.message)
        ], [
            'FOOBARBAZBAX',
            'committees',
            'http://online.knesset.gov.il/WsinternetSps/KnessetDataService/CommitteeScheduleData.svc/FOOBARBAZBAX?CommitteeId=%271%27&FromDate=%272016-01-01T00%3A00%3A00%27',
            "('Connection aborted.', error(104, 'Connection reset by peer'))",
        ])
