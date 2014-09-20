# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fiddle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('html', models.CharField(max_length=255)),
                ('javascript', models.CharField(max_length=255)),
                ('css', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Genres',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(unique=True, max_length=255)),
                ('password', models.CharField(default=None, max_length=255, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProfilePic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('profpic', models.FileField(upload_to=b'images/')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Rating_show',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rating', models.DecimalField(max_digits=5, decimal_places=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Review_show',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('review', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Shows',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('poster', models.CharField(max_length=255)),
                ('summary', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Shows_genres',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('genre', models.ForeignKey(to='chefeditor.Genres')),
                ('show', models.ForeignKey(to='chefeditor.Shows')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('profile_pic', models.CharField(max_length=255)),
                ('login', models.ForeignKey(to='chefeditor.Login')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='review_show',
            name='show',
            field=models.ForeignKey(to='chefeditor.Shows'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='review_show',
            name='user',
            field=models.ForeignKey(to='chefeditor.Users'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='rating_show',
            name='show',
            field=models.ForeignKey(to='chefeditor.Shows'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='rating_show',
            name='user',
            field=models.ForeignKey(to='chefeditor.Users'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fiddle',
            name='login',
            field=models.ForeignKey(to='chefeditor.Login'),
            preserve_default=True,
        ),
    ]
