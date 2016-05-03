# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sender', models.CharField(default=b'', max_length=200)),
                ('email', models.EmailField(default=b'', max_length=200)),
                ('subject', models.CharField(default=b'', max_length=200)),
                ('message', models.CharField(default=b'', max_length=1000)),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ['-datetime'],
            },
        ),
    ]
