#!/usr/bin/env bash

# this script should run from knesset-data/python directory

if [ "$1" == "" ] ; then
    echo "usage: $0 <type>"
    echo "<type> = initial or periodic"
else
    PYTHONPATH=. python knesset_data/dataservice/monitor/metadata/$1.py
fi
