# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_create', models.DateTimeField(auto_now=True, verbose_name=b'Date of Registry')),
                ('member', models.ForeignKey(verbose_name=b'Member', to='coffee.Member')),
            ],
            options={
                'ordering': ['date_create'],
                'verbose_name': 'Registry',
                'verbose_name_plural': 'Registries',
            },
        ),
    ]
