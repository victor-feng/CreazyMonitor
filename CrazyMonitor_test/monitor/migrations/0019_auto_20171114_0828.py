# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-14 08:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0018_auto_20160525_0737'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActionCondtion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logic_type', models.CharField(blank=True, choices=[(b'or', b'OR'), (b'and', b'AND')], max_length=32, null=True, verbose_name='\u4e0e\u4e00\u4e2a\u6761\u4ef6\u7684\u903b\u8f91\u5173\u7cfb')),
                ('action', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitor.Action', verbose_name='\u5c5e\u4e8e\u54ea\u4e2aaction')),
                ('trigger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitor.Trigger', verbose_name='\u6240\u5173\u8054\u7684trigger')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='actioncondtion',
            unique_together=set([('action', 'trigger')]),
        ),
    ]
