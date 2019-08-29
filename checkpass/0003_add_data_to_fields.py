#scrapers/apps/fda/migrations
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations

from scrapers.apps.base.migrations import update_portals


def load_data(apps, schema_editor):
    update_portals(
        apps=apps,
        json_list=['0003_add_data_to_fields.json'],
        base_fields=['name', 'iso2_code'],
        update_fields=['login_url', 'logout_url', 'headers'],
        app_name='fda',
    )


class Migration(migrations.Migration):

    dependencies = [
        ('fda', '0002_transformer_validator'),
    ]

    operations = [
        migrations.RunPython(load_data),
    ]