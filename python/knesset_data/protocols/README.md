# Knesset Protocol File Parsers

## Plenum
* Parses the protocol text to get some metadata from the plenum files, e.g. [20_ptm_318579.doc](/python/knesset_data/protocols/tests/20_ptm_318579.doc)
* See [knesset_data/protocols/tests/test_plenum.py](/python/knesset_data/protocols/tests/test_plenum.py) for usage example.

## Committee Meeting
* Parses the text, divides into parts and speakers, identify attending members.
* See [knesset_data/protocols/tests/test_committee.py](/python/knesset_data/protocols/tests/test_committee.py) for usage example.
