#!/usr/bin/env bash

set -e  # exit on errors

pushd python > /dev/null
    echo "Running python tests"
    bin/run_tests.sh
popd > /dev/null

pushd django > /dev/null
    echo "Running django tests"
    ./manage.py test

    echo "syncdb and migrate from scratch - to test migrations (might take a while..)"
    ./manage.py syncdb --noinput
    ./manage.py migrate
popd > /dev/null
