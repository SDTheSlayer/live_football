# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scores', '0002_auto_20190120_1650'),
    ]

    operations = [
        migrations.AddField(
            model_name='scores',
            name='time',
            field=models.CharField(max_length=10, default=1),
            preserve_default=False,
        ),
    ]
