# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-29 13:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manual_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='additionaltools',
            name='node',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='manual_app.Nodes'),
        ),
    ]