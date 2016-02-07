from knesset_data.dataservice.constants import SERVICE_URLS
import requests
from requests.exceptions import RequestException
import os
from octohub.connection import Connection as OctohubConnection
import logging
import sys
import json


logger = logging.getLogger('knesset_data.dataservice.monitor.metadata')

def github_add_or_update_issue(title, msg, gist_files=None):
    token = os.environ.get('KNESSET_DATA_GITHUB_TOKEN', None)
    if token:
        title = 'monitor: %s'%title
        github = OctohubConnection(token)
        if gist_files:
            res = github.send('POST', '/gists', data=json.dumps({
                "description": "automatically created gist from knesset-data health monitor ",
                "files": gist_files
            }))
            gist_id = res.parsed['id']
            gist_url = "https://gist.github.com/OriHoch/%s"%gist_id
            msg += "\n\nfor more details see: "+gist_url
        search_query = 'is:issue is:open label:"auto-created by monitor" "%s"'%title
        res = github.send('GET', '/search/issues', params={'q': search_query})
        if len(res.parsed['items']) > 0:
            issue_number = res.parsed['items'][0]['number']
            github.send('POST', '/repos/hasadna/knesset-data/issues/%s/comments'%issue_number, data=json.dumps({
                'body': "_**Encountered the error again**_\n\n%s"%msg,
            }))
        else:
            github.send('POST', '/repos/hasadna/knesset-data/issues', data=json.dumps({
                'title': title,
                'body': "_**This issue was automatically created by the [knesset-data health monitor](https://github.com/hasadna/knesset-data/tree/master/python/knesset_data/dataservice/monitor), please do not modify the title or remove any labels**_\n\n%s"%msg,
                'labels': ["auto-created by monitor","Knesset bug"],
            }))


def notify_error(name, url, msg, content):
    logger.error('error in %s service: %s\nurl=%s\ncontent=%s'%(name,msg, url, content))
    github_add_or_update_issue(
        'error while fetching metadata for %s service'%name,
        "unexpected error while trying to fetch metadata for %s service\n\nurl=%s\n\nerror=%s\n\n%s"%(name, url, msg, content)
    )

def notify_xml_changed(name, url, original, updated):
    logger.warning('xml changed in %s service\nurl=%s'%(name, url))
    github_add_or_update_issue(
        "metadata changed for %s service"%name,
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
