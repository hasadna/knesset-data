## Data

An important part of Knesset-Aata project is to document and test the actual Knesset Data.

We have documentation of the available Knesset APIs and Data.

You can help to:

* **improve the existing documentation**
* **test and document missing details**
* **[issues on our issue tracker](https://github.com/hasadna/knesset-data/issues)**

## Code

Currently we have a Python interface. You can extend it or write other interfaces, JS is pretty cool now, why not write an interface for it?

* **[see the list of issues on our issue tracker](https://github.com/hasadna/knesset-data/issues)**

## Project administration

#### Release a new release

* merge some pull requests
* create a new draft release (https://github.com/hasadna/knesset-data/releases)
  * update the release notes, save draft
* edit [/python/setup.py](/python/setup.py)
  * update the version to match the version in the GitHub draft release
* publish the version to pypi
  * `$ cd knesset-data/python`
  * `knesset-data/python$ bin/update_pypi.sh`
* commit and push the version change
  * `knesset-data/python$ git commit -m ""`