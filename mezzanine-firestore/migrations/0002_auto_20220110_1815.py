# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2022-01-10 18:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mezzanine_firestore', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='firestoreID',
            field=models.CharField(blank=True, default='0', max_length=128, unique=True),
        ),
    ]
