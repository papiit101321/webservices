# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2022-01-10 18:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mezzanine_firestore', '0003_auto_20220110_1817'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='firestoreID2',
            new_name='firestoreID',
        ),
    ]
