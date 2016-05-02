# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'Name')),
                ('email', models.EmailField(max_length=254, verbose_name=b'Email')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Member',
                'verbose_name_plural': 'Members',
            },
        ),
    ]
