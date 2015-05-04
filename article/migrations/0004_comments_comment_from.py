# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
from random import randrange


class Migration(migrations.Migration):
    def forwards(self, orm):
        comments = orm.Comments.all()
        for comment in comments:
            rand = randrange(1, 2)
            comment.comment_from = orm['auth.User'].objects.get(id = rand)
            comment.save()
    def backward(self, orm):
        pass


    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article', '0003_article_article_dislikes'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='comment_from',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
