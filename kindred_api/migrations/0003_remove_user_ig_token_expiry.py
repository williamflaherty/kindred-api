# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kindred_api', '0002_auto_20150725_2011'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='ig_token_expiry',
        ),
    ]
