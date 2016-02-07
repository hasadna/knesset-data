#!/usr/bin/env bash

if [ "$1" == "" ] ; then
    echo "usage: $0 <type>"
    echo "<type> = initial or periodic"
else
    DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
    pushd $DIR/..  > /dev/null
    PYTHONPATH=. python knesset_data/dataservice/monitor/metadata/$1.py
    popd  > /dev/null
fi
