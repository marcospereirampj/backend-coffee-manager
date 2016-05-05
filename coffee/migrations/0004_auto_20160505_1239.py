# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0003_auto_20160502_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registry',
            name='member',
            field=models.ForeignKey(related_name='registries', verbose_name=b'Member', to='coffee.Member'),
        ),
    ]
