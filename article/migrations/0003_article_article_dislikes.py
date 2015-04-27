# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_remove_article_article_dislikes'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_dislikes',
            field=models.IntegerField(default=0),
        ),
    ]
