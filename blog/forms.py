from django import forms
from . import models

class CreateBlog(models.Model):
  class Meta:
    model = models.Blog
    fields = ['title', 'body']