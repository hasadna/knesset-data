#!/usr/bin/env bash

set -e  # exit on errors

pip install --upgrade pip
pip install -r django/requirements.txt
pip install -r python/requirements.txt
pip install python/
pip install django/
pip install https://github.com/OriHoch/Open-Knesset/archive/move-refactor-data-gathering-and-model-to-knesset-data.zip#egg=Open-Knesset
