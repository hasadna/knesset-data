#!/usr/bin/env bash

# running an individual test:
# $ bin/run_test.sh knesset_data.dataservice.tests.committees.test_committees

# you can pass any parameter, see the help message:
# $ bin/run_test.sh --help

python -m unittest $*
