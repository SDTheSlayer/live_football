# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scores', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scores',
            name='score1',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='scores',
            name='score2',
            field=models.CharField(max_length=10),
        ),
    ]
