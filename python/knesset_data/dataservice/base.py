from bs4 import BeautifulSoup, Tag
import urllib2
import datetime


class BaseKnessetDataServiceField(object):

    def get_value(self, entry):
        raise Exception('must be implemented by extending classes, should return the value for this field')

    def get_order_by_field(self):
        raise Exception('must be implemented by extending classes if order by support is needed for this field')


class KnessetDataServiceSimpleField(BaseKnessetDataServiceField):

    def __init__(self, knesset_field_name):
        self._knesset_field_name = knesset_field_name

    def get_value(self, entry):
        data = entry['data']
        return data[self._knesset_field_name]

    def get_order_by_field(self):
        return self._knesset_field_name


class BaseKnessetDataServiceObject(object):

    SERVICE_NAME = None
    METHOD_NAME = None
    DEFAULT_ORDER_BY_FIELD = None

    FIELDS = {
        # mapping of (output object field name : knesset field)
    }

    @classmethod
    def _get_service_name(cls):
        return cls.SERVICE_NAME

    @classmethod
    def _get_method_name(cls):
        return cls.METHOD_NAME

    @classmethod
    def _get_url_base(cls):
        return u"http://online.knesset.gov.il/WsinternetSps/KnessetDataService/{service_name}.svc/{method_name}".format(
            service_name=cls._get_service_name(),
            method_name=cls._get_method_name()
        )

    @classmethod
    def _get_url_single(cls, id):
        return u"{url}({id})".format(
            url=cls._get_url_base(),
            id=id
        )

    @classmethod
    def _get_url_page(cls, order_by, results_per_page, page_num):
        url = cls._get_url_base()
        url += '?$top=%s&$skip=%s'%(results_per_page, (page_num-1)*results_per_page)
        if order_by:
            if isinstance(order_by, (list, tuple)):
                order_by = '%s%%20%s'%order_by
            url += '&$orderby=%s'%order_by
        return url

    @classmethod
    def _get_soup(cls, url):
        return BeautifulSoup(urllib2.urlopen(url).read(), 'html.parser')

    @classmethod
    def _parse_entry(cls, entry):
        entry_id = entry.id.string
        entry_links = []
        for link in entry.find_all('link'):
            entry_links.append({'href': link.attrs['href'], 'rel': link.attrs['rel'][0], 'title': link.attrs['title']})
        data = {}
        for prop in entry.content.find('m:properties').children:
            if isinstance(prop, Tag):
                prop_tagtype, prop_name = prop.name.split(':')
                prop_type = prop.attrs.get('m:type', '')
                prop_null = (prop.attrs.get('m:null', '') == 'true')
                if prop_null:
                    prop_val = None
                elif prop_type == '':
                    prop_val = prop.string
                elif prop_type in ('Edm.Int32', 'Edm.Int16', 'Edm.Byte'):
                    prop_val = int(prop.string)
                elif prop_type == 'Edm.Decimal':
                    prop_val = float(prop.string)
                elif prop_type == 'Edm.DateTime':
                    prop_val = datetime.datetime.strptime(prop.string, "%Y-%m-%dT%H:%M:%S")
                else:
                    raise Exception('unknown prop type: %s'%prop_type)
                data[prop_name] = prop_val
        return {
            'id': entry_id,
            'links': entry_links,
            'data': data,
        }

    @classmethod
    def get(cls, id):
        soup = cls._get_soup(cls._get_url_single(id))
        return cls(cls._parse_entry(soup.entry))

    @classmethod
    def get_page(cls, order_by=None, results_per_page=50, page_num=1):
        if not order_by and cls.DEFAULT_ORDER_BY_FIELD:
            order_by = (cls.DEFAULT_ORDER_BY_FIELD, 'desc')
        if order_by:
            order_by_field, order_by_dir = order_by
            order_by_field = cls.FIELDS[order_by_field].get_order_by_field()
            order_by = order_by_field, order_by_dir
        soup = cls._get_soup(cls._get_url_page(order_by, results_per_page, page_num))
        if len(soup.feed.find_all('link', attrs={'rel':'next'})) > 0:
            raise Exception('looks like you asked for too much results per page, 50 results per page usually works')
        else:
            return [cls(cls._parse_entry(entry)) for entry in soup.feed.find_all('entry')]

    def __init__(self, entry):
        self._entry = entry
        for attr_name, field in self.FIELDS.iteritems():
            setattr(self, attr_name, field.get_value(entry))
