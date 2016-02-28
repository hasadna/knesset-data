"""this is not used, see periodic instead"""


from knesset_data.dataservice.constants import SERVICE_URLS
import requests
from requests.exceptions import RequestException
import os


def main():
    for name, url in SERVICE_URLS.iteritems():
        metadata_url = url+'/$metadata'
        filename = os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', 'metadata_xmls', "%s.xml"%name)
        r = requests.get(metadata_url)
        with open(filename, 'wb') as f:
            f.write(r.content)
        # try:
        #     r = requests.get(metadata_url)
        #     if r.status_code == 200:
        #         with open(filename, 'wb') as f:
        #             f.write(r.content)
        #             print 'OK!'
        #     else:
        #         print 'invalid status!'
        # except RequestException, e:
        #     error = str(e)
        #     print error


if __name__ == "__main__":
    main()
