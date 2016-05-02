# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0002_registry'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='registry',
            options={'ordering': ['date_created'], 'verbose_name': 'Registry', 'verbose_name_plural': 'Registries'},
        ),
        migrations.RenameField(
            model_name='registry',
            old_name='date_create',
            new_name='date_created',
        ),
    ]
