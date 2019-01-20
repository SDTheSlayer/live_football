# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='scores',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('team1', models.CharField(max_length=255)),
                ('team2', models.CharField(max_length=255)),
                ('score1', models.IntegerField(max_length=10)),
                ('score2', models.IntegerField(max_length=10)),
            ],
        ),
    ]
