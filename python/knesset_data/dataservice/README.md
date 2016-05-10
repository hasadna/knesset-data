# Knesset Dataservice (OData) APIs

It's a standard [OData](http://www.odata.org/) interface providing access to most Knesset data.

See [constants](/python/knesset_data/dataservice/constants.py) for the definitive list of the available service endpoints

## Services Documentation and Usage Examples

* [Votes](/python/knesset_data/dataservice/VOTES.md)

## Viewing the source data

You can view the data online using [xodata](http://pragmatiqa.com/xodata/):
* in xodata - choose source "metadata url"
* paste the relevant service /$metadata url:
  * laws: http://online.knesset.gov.il/WsinternetSps/KnessetDataService/LawsData.svc/$metadata
  * bills: http://online.knesset.gov.il/WsinternetSps/KnessetDataService/BillsData.svc/$metadata
  * final_laws: http://online.knesset.gov.il/WsinternetSps/KnessetDataService/FinalLawsData.svc/$metadata
  * members: http://online.knesset.gov.il/WsinternetSps/KnessetDataService/KnessetMembersData.svc/$metadata
  * votes: http://online.knesset.gov.il/WsinternetSps/KnessetDataService/VotesData.svc/$metadata
  * committees: http://online.knesset.gov.il/WsinternetSps/KnessetDataService/CommitteeScheduleData.svc/$metadata
  * messages: http://online.knesset.gov.il/WsinternetSps/KnessetDataService/KnessetMessagesData.svc/$metadata
  * mmm: http://online.knesset.gov.il/WsinternetSps/KnessetDataService/MMMData.svc/$metadata
  * lobbyists: http://online.knesset.gov.il/WsinternetSps/KnessetDataService/LobbyistData.svc/$metadata
