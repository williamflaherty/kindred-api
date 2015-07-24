# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('challenge', models.CharField(unique=True, max_length=140)),
                ('pub_date', models.DateTimeField(verbose_name=b'date_published')),
                ('completions', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.CharField(max_length=2083)),
                ('pub_date', models.DateTimeField(verbose_name=b'date_published')),
                ('updoots', models.IntegerField(default=0)),
                ('downvotes', models.IntegerField(default=0)),
                ('instagram', models.BooleanField(default=False)),
                ('flagged', models.BooleanField(default=False)),
                ('city', models.CharField(max_length=85)),
                ('top_tf', models.BooleanField(default=False, verbose_name=b'top_twenty_five')),
                ('challenge', models.ForeignKey(to='kindred_api.Challenge')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=100)),
                ('ig_token', models.CharField(max_length=200)),
                ('ig_token_expiry', models.DateTimeField(verbose_name=b'instagram_token_expiration')),
                ('join_date', models.DateTimeField(verbose_name=b'join_date')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='photo',
            name='user',
            field=models.ForeignKey(to='kindred_api.User'),
            preserve_default=True,
        ),
    ]
