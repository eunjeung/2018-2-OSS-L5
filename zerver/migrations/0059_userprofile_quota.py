# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-04 07:40

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('zerver', '0058_realm_email_changes_disabled'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='quota',
            field=models.IntegerField(default=1073741824),
        ),
    ]
