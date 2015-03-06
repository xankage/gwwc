# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Charity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=128)),
                ('description', models.CharField(max_length=512)),
                ('money_raised', models.IntegerField(default=0)),
                ('people_reached', models.IntegerField(default=0)),
                ('money_used', models.IntegerField(default=0)),
                ('people_used', models.IntegerField(default=0)),
                ('time_used', models.IntegerField(default=0)),
                ('link', models.URLField(max_length=128)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
