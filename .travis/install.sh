#!/usr/bin/env bash

set -e  # exit on errors

pip install --upgrade pip
pip install -r django/requirements.txt
pip install django/
pip install https://github.com/hasadna/Open-Knesset/archive/e28339da7ca92df96fc79b89351286e2715fcff0.zip#egg=Open-Knesset
