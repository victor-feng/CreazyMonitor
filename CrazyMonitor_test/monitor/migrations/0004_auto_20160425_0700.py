# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-25 07:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0003_auto_20160409_0313'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='triggerexpression',
            name='left_sibling',
        ),
        migrations.AddField(
            model_name='triggerexpression',
            name='next_condition',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='right_sibling_condition', to='monitor.TriggerExpression', verbose_name='\u53f3\u8fb9\u6761\u4ef6'),
        ),
    ]
