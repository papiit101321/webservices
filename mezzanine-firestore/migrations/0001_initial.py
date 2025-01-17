# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2022-01-10 18:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firestoreID', models.CharField(blank=True, max_length=128, null=True, unique=True)),
                ('filepath', models.CharField(max_length=512)),
                ('imageURL', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=256, unique=True)),
                ('firestoreID', models.CharField(blank=True, max_length=128, null=True, unique=True)),
                ('title', models.CharField(max_length=256)),
                ('resume', models.CharField(max_length=1024)),
                ('people_on_charge', models.CharField(max_length=128)),
                ('begin_date', models.DateField()),
                ('end_date', models.DateField()),
                ('imageURL', models.URLField(blank=True, max_length=512, null=True)),
                ('updated', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Questionary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quiz', models.CharField(max_length=4096)),
                ('answers', models.CharField(max_length=4096)),
            ],
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=256, unique=True)),
                ('firestoreID', models.CharField(blank=True, max_length=128, null=True, unique=True)),
                ('title', models.CharField(max_length=256)),
                ('people_on_charge', models.CharField(max_length=128)),
                ('date', models.DateField()),
                ('geoposition', models.CharField(max_length=128)),
                ('updated', models.BooleanField(default=False)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mezzanine_firestore.Project')),
            ],
        ),
        migrations.AddField(
            model_name='questionary',
            name='visit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mezzanine_firestore.Visit'),
        ),
        migrations.AddField(
            model_name='photo',
            name='visit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mezzanine_firestore.Visit'),
        ),
        migrations.AddField(
            model_name='label',
            name='photo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mezzanine_firestore.Photo'),
        ),
    ]
