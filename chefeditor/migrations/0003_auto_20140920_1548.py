# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chefeditor', '0002_auto_20140917_1248'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating_show',
            name='show',
        ),
        migrations.RemoveField(
            model_name='rating_show',
            name='user',
        ),
        migrations.DeleteModel(
            name='Rating_show',
        ),
        migrations.RemoveField(
            model_name='review_show',
            name='show',
        ),
        migrations.RemoveField(
            model_name='review_show',
            name='user',
        ),
        migrations.DeleteModel(
            name='Review_show',
        ),
        migrations.RemoveField(
            model_name='shows_genres',
            name='genre',
        ),
        migrations.DeleteModel(
            name='Genres',
        ),
        migrations.RemoveField(
            model_name='shows_genres',
            name='show',
        ),
        migrations.DeleteModel(
            name='Shows',
        ),
        migrations.DeleteModel(
            name='Shows_genres',
        ),
    ]
