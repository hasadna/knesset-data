#!/usr/bin/env bash

# runs a monitor that ensures the knesset dataservice metadata hasn't changed
# if a change is detected - a github issue is automatically created (assuming you set the right GitHub OAuth environment variables)

if [ "$1" == "" ] ; then
    echo "usage: $0 <type>"
    echo "<type> = initial or periodic"
else
    DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
    pushd $DIR/..  > /dev/null
    PYTHONPATH=. python knesset_data/dataservice/monitor/metadata/$1.py
    popd  > /dev/null
fi
