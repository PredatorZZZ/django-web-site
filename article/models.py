# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.contrib import auth

# Create your models here.
class Article(models.Model):
    class Meta():
        db_table = "article"
    article_title = models.CharField(max_length=200)
    article_text = models.TextField()
    article_date = models.DateTimeField(auto_now_add=True)
    article_likes = models.IntegerField(default=0)
    article_dislikes = models.IntegerField(default=0)
    article_images = models.ImageField(
        upload_to="static/uploaded_images/",
        verbose_name=u'your_picture',
        help_text='150x150x',
        default=None
    )


class Comments(models.Model):
    class Meta():
        db_table = "comments"
    comment_article = models.ForeignKey(Article)
    comment_text = models.TextField(max_length=500, verbose_name='Текст комментария')
    comment_date = models.DateTimeField(auto_now=True)
    comment_from = models.ForeignKey(User)

