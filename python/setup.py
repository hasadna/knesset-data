#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='knesset-dataservice',
    version='0.0.1',
    description='API to the Knesset (Israely parliament) data service',
    author='Ori Hoch',
    author_email='ori@uumpa.com',
    license='GPLv3',
    url='https://github.com/hasadna/knesset-dataservice',
    packages=find_packages(exclude=["tests", "test.*"]),
    install_requires=['beautifulsoup4']
)
