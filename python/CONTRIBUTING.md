 knesset-data==1.2.0## Data

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

#### Publishing a release

* merge some pull requests
* create a new draft release (https://github.com/hasadna/knesset-data/releases)
  * update the release notes, save draft
* edit [/python/setup.py](/python/setup.py)
  * update the version to match the version in the GitHub draft release
* publish the version to pypi
  * `$ cd knesset-data/python`
  * `knesset-data/python$ bin/update_pypi.sh`
* commit and push the version change
  * `knesset-data/python$ git commit -am "bump version to ..."`
  * `knesset-data/python$ git push hasadna master`
* publish the release on GitHub

#### Updating Open Knesset

After publishing a release you probably want to update it in Open-Knesset

In Open Knesset repository -

* edit [Open-Knesset/requirements.txt](https://github.com/hasadna/Open-Knesset/blob/master/requirements.txt)
* `knesset-data==1.2.0`
* test and open a pull request in Open Knesset
