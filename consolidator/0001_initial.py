#scrapers/apps/proconsumo/migrations/0001_initial.py

from __future__ import unicode_literals
from django.db import migrations
from scrapers.apps.base.migrations import load_portals


def load_data(apps, schema_editor):
    load_portals(apps=apps, json_list=['0001_basic_portal_info.json'], app_name='proconsumo')


class Migration(migrations.Migration):
    dependencies = [
        ('base', '0079_auto_20190703_0943'),
    ]
    operations = [
        migrations.RunPython(load_data),
    ]
