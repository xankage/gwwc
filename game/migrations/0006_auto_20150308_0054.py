# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0005_auto_20150306_2050'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128)),
                ('link', models.CharField(max_length=128)),
                ('charity', models.ForeignKey(to='game.Charity')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name_plural': 'people'},
        ),
        migrations.AlterModelOptions(
            name='site',
            options={},
        ),
        migrations.AlterField(
            model_name='charity',
            name='link',
            field=models.CharField(max_length=128),
        ),
    ]
