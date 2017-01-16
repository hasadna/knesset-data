# encoding: utf-8
import csv
import sys
from knesset_data_django.common.management_commands.base_knesset_dataservice_command import BaseKnessetDataserviceCommand
from optparse import make_option
from knesset_data_django.common.management_commands.exceptions import BaseScraperException, ReachedMaxItemsException


class BaseKnessetDataserviceCollectionCommand(BaseKnessetDataserviceCommand):
    DATASERVICE_CLASS = None

    option_list = BaseKnessetDataserviceCommand.option_list + (
        make_option('--page-range', dest='pagerange', default='1-10',
                    help="range of page number to scrape (e.g. --page-range=5-12), default is 1-10"),
        make_option('--max-items', dest='maxitems', default='0',
                    help='maximum number of items to process'),
        make_option('--re-create', dest='recreate', default='',
                    help='comma-separated item ids to delete and then re-create'),
        make_option('--validate-pages', dest='validatepages',
                    help="validate objects between (and including) given page range\npages in this case are based on ascending ordering, so you'll have the same page numbers each time"),
        make_option('--validate-skip-to', dest='validateskipto',
                    help="skip to the given object id (for use with --validate-pages)"),
        make_option('--create-src-id', dest='createsrcid',
                    help="create the given object/s from the comma-separated src ids (assuming they don't already exist in DB)"),
        make_option('--validate-output-file', dest='validateoutputfile',
                    help="where to write the validation results to (defaults to stdout)"),
        make_option('--validate-fix', dest='validatefix', action='store_true',
                    help="try to fix some problems directly in DB which are safe to automatically fix")
    )

    def _handle_page(self, page_num):
        for dataservice_object in self.DATASERVICE_CLASS.get_page(page_num=page_num):
            if not self._has_existing_object(dataservice_object):
                oknesset_obj = self._create_new_object(dataservice_object)
                self.logger.debug(u'created new object %s: %s' % (oknesset_obj.pk, oknesset_obj))
                if self._max_items > 0:
                    self._num_items += 1
                    if self._num_items == self._max_items:
                        raise ReachedMaxItemsException('reached maxitems')

    def _handle_recreate(self, options):
        self.logger.info('recreating objects %s' % options['recreate'])
        recreated_objects = self.recreate_objects(
            [int(id) for id in options['recreate'].split(',')])
        self.logger.info(
            'created as objects %s' % (','.join([str(o.pk) for o in recreated_objects]),))

    def _handle_createsrcid(self, options):
        src_ids = [int(i) for i in options['createsrcid'].split(',')]
        self.logger.info('downloading %s objects'%len(src_ids))
        dataservice_objects = []
        for src_id in src_ids:
            self.logger.info('downloading object %s'%src_id)
            dataservice_object = self.DATASERVICE_CLASS.get(src_id)
            dataservice_objects.append(dataservice_object)
        self.logger.info('downloaded all objects data, will create them now')
        oknesset_objects = []
        for dataservice_object in dataservice_objects:
            if self._has_existing_object(dataservice_object):
                raise BaseScraperException('object already exists in DB: %s'%dataservice_object.id)
            else:
                oknesset_object = self._create_new_object(dataservice_object)
                oknesset_objects.append(oknesset_object)
                self.logger.info('created object %s (%s)'%(oknesset_object, oknesset_object.pk))
        self.logger.info('done, created %s objects'%len(oknesset_objects))

    def _get_validate_header_row(self):
        return ['knesset object id', 'open knesset object id', 'error']

    def _get_validate_error_row(self, dataservice_object, oknesset_object, error):
        return [dataservice_object.id, oknesset_object.id if oknesset_object else '', error]

    def _get_validate_order_by(self):
        return 'id', 'asc'

    def _get_validate_first_object_title(self, dataservice_object):
        return 'src_id: %s'%dataservice_object.id

    def _get_dataservice_model_kwargs(self, dataservice_object):
        if not hasattr(self, 'DATASERVICE_MODEL_MAP'):
            raise NotImplementedError('DATASERVICE_MODEL_MAP should be defined, or override _get_dataservice_model_kwargs')
        else:
            return {
                k: getattr(dataservice_object, v) if isinstance(v, str) else v(dataservice_object)
                for k,v in self.DATASERVICE_MODEL_MAP.iteritems()
            }

    def _validate_attr_actual_expected(self, attr_name, actual_value, expected_value):
        # this method allows extending classes to use other comparison for specific attrs
        return actual_value == expected_value

    def _validate_dataservice_object(self, dataservice_object, writer, fix=False):
        # check the basic metadata
        oknesset_object = self._get_existing_object(dataservice_object)
        if oknesset_object is None:
            if fix:
                self.logger.info('could not find corresponding object in DB, creating it now')
                self._create_new_object(dataservice_object)
            else:
                error = 'could not find corresponding object in DB'
                self.logger.warn(error)
                writer.writerow(self._get_validate_error_row(dataservice_object, None, error.encode('utf-8')))
        else:
            for attr_name, expected_value in self._get_dataservice_model_kwargs(dataservice_object).iteritems():
                actual_value = getattr(oknesset_object, attr_name)
                if not self._validate_attr_actual_expected(attr_name, actual_value, expected_value):
                    if fix and attr_name in getattr(self, 'VALIDATE_FIELDS_TO_AUTOFIX', []):
                        self.logger.info('fixing mismatch in %s attribute'%(attr_name,))
                        setattr(oknesset_object, attr_name, expected_value)
                        oknesset_object.save()
                    else:
                        error = 'value mismatch for %s (expected="%s", actual="%s")'%(attr_name, expected_value, actual_value)
                        self.logger.warn(error)
                        writer.writerow(self._get_validate_error_row(dataservice_object, oknesset_object, error.encode('utf-8')))
            error = self._validate_dataservice_oknesset_object(dataservice_object, oknesset_object, writer, fix)
            if error:
                self.logger.warn(error)
                writer.writerow([dataservice_object.id, oknesset_object.id, error.encode('utf-8')])

    def _validate_dataservice_oknesset_object(self, dataservice_object, oknesset_object, writer, fix):
        # allows extending classes to add custom validations, extending classes can either return an error string which will be written
        # or, optionally - add rows directly to the writer, allowing more flexibility
        return None

    def _validate_pages(self, out, pages, skip_to_src_id, try_to_fix):
        writer = csv.writer(out)
        writer.writerow(self._get_validate_header_row())
        for page in pages:
            self.logger.info('downloading page %s'%page)
            dataservice_objects = self.DATASERVICE_CLASS.get_page(order_by=self._get_validate_order_by(), page_num=page)
            self.logger.info('downloaded %s votes'%len(dataservice_objects))
            if len(dataservice_objects) < 1:
                self.logger.warn('no objects in the page')
            else:
                self.logger.info('  first object %s'%self._get_validate_first_object_title(dataservice_objects[0]))
                for dataservice_object in dataservice_objects:
                    if not skip_to_src_id or int(dataservice_object.id) >= int(skip_to_src_id):
                        self.logger.info('validating object src_id %s'%dataservice_object.id)
                        self._validate_dataservice_object(dataservice_object, writer, fix=try_to_fix)

    def _handle_validatepages(self, options):
        from_page, to_page = [int(p) for p in options['validatepages'].split('-')]
        skip_to_src_id = options.get('validateskipto', None)
        output_file_name = options.get('validateoutputfile', None)
        try_to_fix = options.get('validatefix', False)
        if from_page > to_page:
            # we support reverse pages as well!
            pages = reversed(range(to_page, from_page+1))
        else:
            pages = range(from_page, to_page+1)
        if output_file_name:
            out = open(output_file_name, 'wb')
        else:
            out = sys.stdout
        self._validate_pages(out, pages, skip_to_src_id, try_to_fix)
        if output_file_name:
            out.close()
        self.logger.info('done')

    def _handle_pagerange(self, options):
        page_range = options['pagerange']
        first, last = map(int, page_range.split('-'))
        self._max_items = int(options['maxitems'])
        self._num_items = 0
        for page_num in range(first, last + 1):
            self.logger.debug('page %s' % page_num)
            try:
                self._handle_page(page_num)
            except ReachedMaxItemsException:
                break

    def handle_noargs(self, **options):
        super(BaseKnessetDataserviceCollectionCommand, self).handle_noargs(**options)
        try:
            if options['recreate'] != '':
                self._handle_recreate(options)
            elif options.get('createsrcid'):
                self._handle_createsrcid(options)
            elif options.get('validatepages'):
                self._handle_validatepages(options)
            elif options.get('pagerange'):
                self._handle_pagerange(options)
        except Exception:
            self.logger.exception('DATASERVICE scraper command UnCaughtException with options %s' % options)
        else:
            raise TypeError('invalid arguments')
