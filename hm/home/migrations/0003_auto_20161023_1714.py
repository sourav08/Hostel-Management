# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-23 11:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_hostel'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Complaints',
            new_name='Complaint',
        ),
    ]
