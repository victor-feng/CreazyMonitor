# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-14 08:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0021_auto_20171114_0834'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='actioncondtion',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='actioncondtion',
            name='action',
        ),
        migrations.RemoveField(
            model_name='actioncondtion',
            name='trigger',
        ),
        migrations.DeleteModel(
            name='ActionCondtion',
        ),
    ]
