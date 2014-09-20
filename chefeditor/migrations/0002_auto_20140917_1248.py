# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chefeditor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fiddle',
            name='public_temp',
            field=models.DecimalField(default=0, max_digits=3, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profilepic',
            name='login',
            field=models.ForeignKey(to='chefeditor.Login', null=True),
            preserve_default=True,
        ),
    ]
