knesset-data
============

A python module that provides api to available Israeli Parliament (Knesset) data

### Installation
* $ pip install knesset-data

### Usage Example
* $ python
* >>> from knesset_data.dataservice.committees import Committee
* >>> committees = Committee.get_all_active_committees()
* >>> len(committees)
* 19
* >>> print committees[0].name
* ועדת הכנסת
