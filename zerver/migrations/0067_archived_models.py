# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-26 01:10

import bitfield.models
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models

import zerver.lib.str_utils

class Migration(migrations.Migration):

    dependencies = [
        ('zerver', '0066_realm_inline_url_embed_preview'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArchivedAttachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.TextField(db_index=True)),
                ('path_id', models.TextField(db_index=True)),
                ('is_realm_public', models.BooleanField(default=False)),
                ('create_time', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('size', models.IntegerField(null=True)),
                ('archive_timestamp', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ArchivedMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(db_index=True, max_length=60)),
                ('content', models.TextField()),
                ('rendered_content', models.TextField(null=True)),
                ('rendered_content_version', models.IntegerField(null=True)),
                ('pub_date', models.DateTimeField(db_index=True, verbose_name='date published')),
                ('last_edit_time', models.DateTimeField(null=True)),
                ('edit_history', models.TextField(null=True)),
                ('has_attachment', models.BooleanField(db_index=True, default=False)),
                ('has_image', models.BooleanField(db_index=True, default=False)),
                ('has_link', models.BooleanField(db_index=True, default=False)),
                ('archive_timestamp', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zerver.Recipient')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('sending_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zerver.Client')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ArchivedUserMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flags', bitfield.models.BitField(['read', 'starred', 'collapsed', 'mentioned', 'wildcard_mentioned', 'summarize_in_home', 'summarize_in_stream', 'force_expand', 'force_collapse', 'has_alert_word', 'historical', 'is_me_message'], default=0)),
                ('archive_timestamp', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zerver.ArchivedMessage')),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='archivedattachment',
            name='messages',
            field=models.ManyToManyField(to='zerver.ArchivedMessage'),
        ),
        migrations.AddField(
            model_name='archivedattachment',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='archivedattachment',
            name='realm',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='zerver.Realm'),
        ),
        migrations.AlterUniqueTogether(
            name='archivedusermessage',
            unique_together=set([('user_profile', 'message')]),
        ),
    ]
