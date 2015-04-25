
# -*- coding: utf-8 -*-
__author__ = 'predator'

from django.forms import ModelForm
from models import Comments

class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['comment_text']