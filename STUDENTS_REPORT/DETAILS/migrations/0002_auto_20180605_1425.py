# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-05 14:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DETAILS', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SubjectFaculty',
            new_name='Subject',
        ),
    ]
