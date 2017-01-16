# Django-specific APis and modules

This directory contains APIs and Python modules specific to usage with Django.

Specifically, it means usage by Open Knesset, but we try to be as separate from it as possible.

### Integrating with existing Django project (AKA Open Knesset)

##### preconditions / assumptions

* existing project is in directory /home/user/Open-Knesset
* existing project is inside a virtualenv called "oknesset"
* clone of knesset-data git repo is in /home/user/knesset-data

##### installation


* install knesset-data and knesset-data-django in the existing project virtualenv
  * `(oknesset) ~/Open-Knesset$ pip install -e ../knesset-data/python`
  * `(oknesset) ~/Open-Knesset$ pip install -e ../knesset-data/django`
* add relevant the knesset-data-django apps to INSTALLED_APPS -
  * `(oknesset) ~/Open-Knesset$ `
