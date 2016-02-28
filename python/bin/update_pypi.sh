#!/usr/bin/env bash

# update the version on pypi
# assumes pypi authentication is setup with relevant permissions

./setup.py sdist upload
