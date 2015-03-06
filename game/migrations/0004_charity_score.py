# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_auto_20150304_1554'),
    ]

    operations = [
        migrations.AddField(
            model_name='charity',
            name='score',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
