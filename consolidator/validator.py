#scrapers/apps/consolidator/validator/validator.py

# -*- coding: utf-8 -*-
import re

from copy import deepcopy
from goodtables import validate
from tableschema import Table
from slugify import slugify

from .exceptions import ValidatorException
from .properties import props
from scrapers.apps.base.utils.file_services import FileServices


class Validator:

    SKIP_CHECKS = (
        'duplicate-header',
        'duplicate-row',
        'source-error',
        'blank-header',
    )

    def __init__(self, portal):
        assert portal.validation, \
            'Validation config not exists. ' \
            'Hint: Add data migration with appropiate config as JSON and insert case scrapers. ' \
            'Manage command `infer_validator_cofig` is very useful for build config'

        self.portal = portal

    def validate_schema(self, file_path, validation_key):
        assert validation_key in self.portal.validation, \
            '%s not exist, add new entry config to validation column' % validation_key

        if validation_key not in self.portal.validation:
            raise ValueError('error-no-implemented')

        encoding = FileServices.infer_encoding(file_path)
        if encoding in props['not-found-encoding'].keys():
            encoding = props['not-found-encoding'][encoding]

        final_validation = self.build_final_validation(
            file_path=file_path,
            validation_key=validation_key,
            encoding=encoding,
        )

        report = validate(
            file_path,
            schema=final_validation,
            skip_checks=self.SKIP_CHECKS,
            encoding=encoding,
        )
        self._check_report(report)

    def build_final_validation(self, file_path, validation_key, **kwargs):
        """
        Build the final validation (a.k.a descriptor) dict.
        Params:
        :(str) file_path:       File will be validate
        :(dict) validation_key: Each object in array represents 1 column in the file_path, a.k.a.
                                field-descriptor.
        struct is like:
        {
          "name": "name of field (e.g. column_name)",
          "regex_name": "regex for name of field (e.g. column_number_\\d+)",  # Alternative to"name"
          "title": "A nicer human readable label or title for the field",
          "type": "A string specifying the type",
          "format": "A string specifying a format",
          "description": "A description for the field",
          "constraints": {
              # a constraints-descriptor
          }
        }
        For more options read the docs "Description section" in
        https://frictionlessdata.io/specs/table-schema/#descriptor

        :return:
        """
        new_validation = deepcopy(self.portal.validation[validation_key])
        column_names = self._get_columns_names(file_path, **kwargs)

        for idx, column_name in enumerate(column_names):
            if new_validation['fields'][idx].get('name') != column_name:
                """ Options for non matching:
                    * name descriptor has a different char case
                    * name descriptor will be defined by regex_name
                    * field-descriptor is optional and not exists in column_names
                """
                if slugify(new_validation['fields'][idx].get('name', '')) == slugify(column_name):
                    new_validation['fields'][idx]['name'] = column_name

                elif new_validation['fields'][idx].get('regex_name'):
                    search = re.search(
                        pattern=new_validation['fields'][idx].get('regex_name'),
                        string=column_name,
                        flags=re.IGNORECASE,
                    )
                    if search:
                        new_validation['fields'][idx].update({'name': column_name})

                elif new_validation['fields'][idx].get('optional', False):
                    del new_validation['fields'][idx]

        # Review optional field descriptors.
        if idx + 1 < len(new_validation['fields']):
            for field_descriptor in reversed(new_validation['fields']):
                if field_descriptor.get('optional', False):
                    if field_descriptor.get('name') not in column_names:
                        new_validation['fields'].remove(field_descriptor)

        return new_validation

    def _check_report(self, report):
        if not report['valid']:
            for error in report['tables'][0]['errors']:
                if error['code'] not in self.SKIP_CHECKS:
                    raise ValidatorException(report)

    def _get_columns_names(self, file_path, **kwargs):
        table = Table(file_path, **kwargs)
        table.read(keyed=True, limit=1)
        return [field['name'] for field in table.infer()['fields']]
