# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-20 09:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0011_auto_20160220_0905'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aboutentry',
            old_name='new_slug',
            new_name='slug',
        ),
        migrations.RenameField(
            model_name='categoryentry',
            old_name='new_slug',
            new_name='slug',
        ),
        migrations.RenameField(
            model_name='commonentry',
            old_name='new_slug',
            new_name='slug',
        ),
        migrations.RenameField(
            model_name='newsentry',
            old_name='new_slug',
            new_name='slug',
        ),
        migrations.RenameField(
            model_name='sponsorshipentry',
            old_name='new_slug',
            new_name='slug',
        ),
    ]
