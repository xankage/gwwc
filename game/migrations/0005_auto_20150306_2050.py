# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_charity_score'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='site',
            options={'verbose_name_plural': 'people'},
        ),
        migrations.AlterField(
            model_name='charity',
            name='description',
            field=models.CharField(max_length=1024),
        ),
    ]
