"""verifies each knesset dataservice metadata has not changed

if a change is detected - a github issue is automatically opened (assuming GitHub OAuth is setup properly)

runs from bin/metadata_monitor.sh
"""

from knesset_data.dataservice.constants import SERVICE_URLS
import requests
from requests.exceptions import RequestException
import os
import logging
import sys
from knesset_data.utils.github import github_add_or_update_issue


logger = logging.getLogger('knesset_data.dataservice.monitor.metadata')


def notify_error(name, url, msg, content):
    logger.error('error in %s service: %s\nurl=%s\ncontent=%s'%(name,msg, url, content))
    github_add_or_update_issue(
        'monitor: error while fetching metadata for %s service'%name,
        "unexpected error while trying to fetch metadata for %s service\n\nurl=%s\n\nerror=%s\n\n%s"%(name, url, msg, content)
    )

def notify_xml_changed(name, url, original, updated):
    logger.warning('xml changed in %s service\nurl=%s'%(name, url))
    github_add_or_update_issue(
        "monitor: metadata changed for %s service"%name,
        "change detected in metadata of %s service\n\nurl=%s"%(name, url),
        {
            "updated.xml": {"content": updated},
            "original.xml": {"content": original}
        }
    )

def main():
    for name, url in SERVICE_URLS.iteritems():
        metadata_url = url+'/$metadata'
        original_filename = os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', 'metadata_xmls', "%s.xml"%name)
        try:
            r = requests.get(metadata_url)
            if r.status_code == 200:
                with open(original_filename, 'r') as f:
                    original_xml = f.read()
                if r.content != original_xml:
                    notify_xml_changed(name, url, original_xml, r.content)
                else:
                    logger.info('service %s metadata was not changed'%name)
            else:
                notify_error(name, url, 'invalid status code', r.status_code)
        except RequestException, e:
            notify_error(name, url, 'request exception', str(e))

if __name__ == "__main__":
    logging.basicConfig(stream=sys.stdout, level=logging.WARNING)
    main()
