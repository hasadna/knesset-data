# knesset-data

APIs and documentation to allow getting data about the Israeli Parliament (Knesset).

* [Issues](https://github.com/hasadna/knesset-dataservice/issues)
* [Contributing to knesset-data](CONTRIBUTING.md)

### Sub-projects

##### Data sources documentation

* [documentation about the Knesset data sources](/docs/DataSources.md)
* We also track Knesset datasources bugs and known problems - [see issues labeled "Knesset bug"](https://github.com/hasadna/knesset-data/issues?q=is%3Aissue+is%3Aopen+label%3A%22Knesset+bug%22)

##### Knesset datapackage

[![travis-ci build status](https://travis-ci.org/hasadna/knesset-data-datapackage.svg)](https://travis-ci.org/hasadna/knesset-data-datapackage)

* Provides downbladable package with all the Knesset data
* https://github.com/hasadna/knesset-data-datapackage

##### Low level Python API

[![travis-ci build status](https://travis-ci.org/hasadna/knesset-data-python.svg)](https://travis-ci.org/hasadna/knesset-data-python)

* Provides methods to fetch and parse Knesset data using Python.
* https://github.com/hasadna/knesset-data-python
* Quickstart:
```
$ pip install knesset-data
python -c "from knesset_data.dataservice.committees import Committee\
print(', '.join([committee.name for committee in Committee.get_all_active_committees()]))
ועדת הכנסת, ועדת הכספים, ועדת הכלכלה, ועדת החוץ ...
```

##### Higher level Django module

[![travis-ci build status](https://travis-ci.org/hasadna/knesset-data-django.svg)](https://travis-ci.org/hasadna/knesset-data-django)

* Store Knesset data in a structured DB and provides logic to handle the DB data.
* https://github.com/hasadna/knesset-data-django
* Quickstart: see the [development guide](https://github.com/hasadna/knesset-data-django/blob/master/DEVELOPMENT.md)

### Known issues / FAQ / Common problems
* check each sub-project's README for FAQ specific to that project
* [How to decide where to move existing code from open knesset?](https://github.com/hasadna/knesset-data/issues/120)
