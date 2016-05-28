# Knesset Laws Dataservice

Returns information about private for preliminary hearing (הצעות חוק פרטיות לדיון מוקדם).

On Knesset website this data is available here: http://knesset.gov.il/privatelaw/Plaw_display.asp?lawtp=1

[Metadata](http://online.knesset.gov.il/WsinternetSps/KnessetDataService/LawsData.svc/$metadata) 
| [Unit Tests](https://github.com/hasadna/knesset-data/tree/master/python/knesset_data/dataservice/tests/laws) 
| [Code](https://github.com/hasadna/knesset-data/blob/master/python/knesset_data/dataservice/laws.py)

## Entities

### privatelaw ([python usage example](https://github.com/hasadna/knesset-data/blob/master/python/knesset_data/dataservice/tests/laws/test_laws.py))

Returns data about the private laws.

#### Known Issues

* https://github.com/hasadna/knesset-data/issues/68
* https://github.com/hasadna/knesset-data/issues/69
* https://github.com/hasadna/knesset-data/issues/70

#### Fields

Field names are mostly self explanatory.

"knesset_id" field is the knesset number and "number" is the number of the law within that knesset.

To get the actual proposal rtf file, you can use the guess_link_url() method but bear in mind that due to bug mentioned above it might not be very reliable.

### privatelaw_mk ([python usage example](https://github.com/hasadna/knesset-data/blob/master/python/knesset_data/dataservice/tests/laws/test_laws.py))

Returns data about the MKs that initiated or joined the private law proposal

#### Fields

"mk_id" field related to the standard mk id as used on official knesset and also on Open-Knesset

"mk_suggest" field contains 1 if the mk suggested the proposal (there can be multiple mks that suggested a proposal)
