# Knesset Dataservice (OData) APIs

It's a standard [OData](http://www.odata.org/) interface providing access to most Knesset data.

## Available source data

There are multiple versions of the Knesset APIs with the newest API replacing the old ones.

### Latest API

The new API was silently launched by Knesset on March 5, 2017 - it is a full re-write of the old APIs and is supposed to be well documented and supported (as much as Knesset can..)

* XOData endpoint http://knesset.gov.il/Odata/ParliamentInfo.svc/$metadata
* [Knesset OData documentation (draft)](https://docs.google.com/document/d/1FHqabNsYlSNyul1lArmnONLHnYGA4XQNMs3k-dPgUok/edit?usp=sharing)

#### Browsing the source data

You can view the data using XOData tools which allows free access for publically accessible endpoints

* Best way is to download the [chrome extension](https://chrome.google.com/webstore/detail/xodata%C2%AE/hpooflanfopjepihkcjjfeonlnhfnmpp)
* Alternatively - you can try to use their [online tool](https://pragmatiqa.com/xodata/) but it doesn't always work..

Open the app - 

* at the top bar - choose access option = ODATA Metadata URL
* paste the metadata url -
  * for the latest API, this is the URL: http://knesset.gov.il/Odata/ParliamentInfo.svc/$metadata
* Click on Get data
* you can now browse the data using the query builder / make direct API requests / view the tables diagram

### Old API versions

* new old APIS
  * הצעות חוק פרטיות לדיון מוקדם: http://knesset.gov.il/Odata_old/LawsData.svc/
  * הצעות חוק שעברו קריאה ראשונה (פרטיות וממשלתיות): http://knesset.gov.il/Odata_old/BillsData.svc/
  * חוקים שהתקבלו לאחר קריאה שלישית: http://knesset.gov.il/Odata_old/FinalLawsData.svc/
  * חברי כנסת, ממשלות וסיעות: http://knesset.gov.il/Odata_old/KnessetMembersData.svc/
  * הצבעות חברי הכנסת במליאה: http://knesset.gov.il/Odata/Votes.svc/
  * מהוועדות - סדרי היום ופרוטוקולים: http://knesset.gov.il/Odata_old/CommitteeScheduleData.svc/
  * הודעות לעיתונות: http://online.knesset.gov.il/WsinternetSps/KnessetDataService/KnessetMessagesData.svc/
  * מרכז מחקר ומידע – מסמכי הממ"מ: http://knesset.gov.il/Odata/MMM.svc/
  * שדלנים: http://knesset.gov.il/Odata/Lobbyists.svc/
  * שאילתות: http://knesset.gov.il/Odata_old/Queries.svc/
  * הצעות חוק לקריאה השנייה והשלישית (פונץ' בננה): http://knesset.gov.il/Odata_old/PunchBananaData.svc/
  * ישיבות המליאה: http://knesset.gov.il/Odata_old/PlmSederYomData.svc/

* old APIS (v3)
  * laws: http://knesset.gov.il/KnessetOdataService/LawsData.svc/
  * bills: http://knesset.gov.il/KnessetOdataService/BillsData.svc/
  * final_laws:  http://knesset.gov.il/KnessetOdataService/FinalLawsData.svc/
  * members: http://knesset.gov.il/KnessetOdataService/KnessetMembersData.svc/
  * votes: http://knesset.gov.il/KnessetOdataService/VotesData.svc/
  * committees: http://knesset.gov.il/KnessetOdataService/CommitteeScheduleData.svc/
  * messages: currently doesn't have a new API
  * mmm: http://knesset.gov.il/KnessetOdataService/MMMData.svc/
  * lobbyists: http://knesset.gov.il/KnessetOdataService/LobbyistODataService.svc/

* Very old APIs
  * laws: http://online.knesset.gov.il/WsinternetSps/KnessetDataService/LawsData.svc/$metadata
  * bills: http://online.knesset.gov.il/WsinternetSps/KnessetDataService/BillsData.svc/$metadata
  * final_laws: http://online.knesset.gov.il/WsinternetSps/KnessetDataService/FinalLawsData.svc/$metadata
  * members: http://online.knesset.gov.il/WsinternetSps/KnessetDataService/KnessetMembersData.svc/$metadata
  * votes: http://online.knesset.gov.il/WsinternetSps/KnessetDataService/VotesData.svc/$metadata
  * committees: http://online.knesset.gov.il/WsinternetSps/KnessetDataService/CommitteeScheduleData.svc/$metadata
  * messages: http://online.knesset.gov.il/WsinternetSps/KnessetDataService/KnessetMessagesData.svc/$metadata
  * mmm: http://online.knesset.gov.il/WsinternetSps/KnessetDataService/MMMData.svc/$metadata
  * lobbyists: http://online.knesset.gov.il/WsinternetSps/KnessetDataService/LobbyistData.svc/$metadata

## Specific services Documentation and Usage Examples

* [Votes](/docs/dataservice/VOTES.md)
* [Laws](/docs/dataservice/LAWS.md)

## See also

* All the knesset APIs are available [here](http://main.knesset.gov.il/Activity/Info/Pages/Databases.aspx)
* See [constants.py](https://github.com/hasadna/knesset-data-python/blob/master/knesset_data/dataservice/constants.py) for the definitive list of the service endpoints we use in the knesset data python implementation
