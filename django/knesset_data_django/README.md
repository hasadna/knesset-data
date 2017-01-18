# knesset_data_django

This document serves as an index of the content of the knesset_data_django package

We (AKA you) try to keep this document updated, but we can't guarantee it..

## documentation

* [How to write scrapers](/django/knesset_data_django/HOW_TO_WRITE_SCRAPERS.md)

## committees

### management commands

  * **[get_committees_data](/django/knesset_data_django/committees/management/commands/get_committees_data.py)**
    * **--members-attendance** - exports a csv file with data about members attendance in committees
  * **[scrape_committees](/django/knesset_data_django/committees/management/commands/scrape_committees.py)** -
    Fetch and update committees data
  * **[scrape_commitee_meetings](/django/knesset_data_django/committees/management/commands/scrape_commitee_meetings.py)** -
    Fetch and update committee meetings data

## models

  * **Committee**
  * **CommitteeMeeting**

## mks (members of Knesset)

### models

  * **Member**
  * **Knesset**

## persons

### models

  * **Person**
  * **PersonAlias**
