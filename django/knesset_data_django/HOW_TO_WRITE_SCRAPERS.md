# How to write scrapers for knesset-data-django

### Scraper objects

Each scraper should have a scraper object.

This is an object that extends [BaseScraper](/django/knesset_data_django/common/scrapers/base_scraper.py)

##### Guidelines

* Scraper objects should output machine readable data about the scraping work that was done.
* Ideally it would be a generator - to allow streaming
  * But, it can also be statistical data.
* The important thing is that the main output of the scraper is machine readable data and not textual output.
* Scraper classes init function is meant to support unit testing - to allow to pass override classes or data to make testing with mocks easier.
* Any external dependency should be inside an overridable function or via init function params.

##### Examples

* [CommitteesScraper](/django/knesset_data_django/committees/scrapers/committees_scraper.py)

### Management commands

Management commands are the way we run the scrapers.

Management commands should extend [BaseNoArgsCommand](/django/knesset_data_django/common/management_commands/base_no_args_command.py).

##### Guildelines

* A management command should have minimal logic and just call the relevant
* It is just a human interface to the scraper.
* It handles getting input about what scraping to do and outputs human readable output.

##### Examples

* [scrape_committees](/django/knesset_data_django/committees/management/commands/scrape_committees.py)
