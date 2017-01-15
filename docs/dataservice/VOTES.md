# Knesset Votes Dataservice

Returns information about votes.

* Python API: [Unit Tests](https://github.com/hasadna/knesset-data/tree/master/python/knesset_data/dataservice/tests/votes) | [Code](https://github.com/hasadna/knesset-data/blob/master/python/knesset_data/dataservice/votes.py)
* [Knesset source $metadata](http://online.knesset.gov.il/WsinternetSps/KnessetDataService/VotesData.svc/$metadata)

## Main Methods

### View_vote_rslts_hdr_Approved ([Python API usage example](https://github.com/hasadna/knesset-data/blob/master/python/knesset_data/dataservice/tests/votes/test_votes.py))

Returns data about the vote.

#### Known Issues
The fields "total_for", "total_against", "total_abstain" might show wrong numbers, please don't rely on them. See [#22](https://github.com/hasadna/knesset-data/issues/22)

To get total vote type numbers, use the [Python API Votes Html Scraper](https://github.com/hasadna/knesset-data/tree/master/python/knesset_data/html_scrapers) - it's more reliable at the moment.


#### Interesting Fields
* vote_id
* knesset_num
* session_id, sess_item_nbr, sess_item_id, sess_item_dscr - details about the plenum session this vote took place in
* vote_date, date, vote_time, time - time/daet of the vote
* is_elctrnc_vote - I think they are all electronic
