# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kindred_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenge',
            name='pub_date',
            field=models.DateField(verbose_name=b'date_published'),
            preserve_default=True,
        ),
    ]
