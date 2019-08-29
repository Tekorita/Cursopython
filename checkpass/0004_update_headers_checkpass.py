from __future__ import unicode_literals
from django.db import migrations
from scrapers.apps.base.migrations import update_portals


def load_data(apps, schema_editor):
    update_portals(
        apps=apps,
        json_list=['0004_update_headers_checkpass.json'],
        base_fields=['name', 'iso2_code'],
        update_fields=['headers'],
        app_name='fda',
    )


class Migration(migrations.Migration):

    dependencies = [
        ('fda', '0003_add_data_to_fields'),
    ]

    operations = [
        migrations.RunPython(load_data),
    ]