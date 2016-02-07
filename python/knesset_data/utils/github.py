import os
from octohub.connection import Connection as OctohubConnection
import json


def github_add_or_update_issue(title, msg, gist_files=None):
    token = os.environ.get('KNESSET_DATA_GITHUB_TOKEN', None)
    if token:
        github = OctohubConnection(token)
        if gist_files:
            res = github.send('POST', '/gists', data=json.dumps({
                "description": "automatically created gist from knesset-data",
                "files": gist_files
            }))
            gist_id = res.parsed['id']
            gist_url = "https://gist.github.com/OriHoch/%s"%gist_id
            msg += "\n\nfor more details see: "+gist_url
        search_query = 'is:issue is:open label:"auto-created" "%s"'%title
        res = github.send('GET', '/search/issues', params={'q': search_query})
        if len(res.parsed['items']) > 0:
            issue_number = res.parsed['items'][0]['number']
            github.send('POST', '/repos/hasadna/knesset-data/issues/%s/comments'%issue_number, data=json.dumps({
                'body': "_**Encountered the error again**_\n\n%s"%msg,
            }))
        else:
            github.send('POST', '/repos/hasadna/knesset-data/issues', data=json.dumps({
                'title': title,
                'body': "_**This issue was automatically created, please do not modify the title or remove any labels**_\n\n%s"%msg,
                'labels': ["auto-created","Knesset bug"],
            }))
