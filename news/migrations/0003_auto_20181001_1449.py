# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-01 11:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_article_article_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='pud_date',
            new_name='pub_date',
        ),
    ]
