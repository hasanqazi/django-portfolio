from django.db import models
from django.contrib.auth.models import User
from djrichtextfield.models import RichTextField

# Create your models here.
class Blog(models.Model):
  title = models.CharField(max_length=60)
  body = RichTextField()
  date = models.DateTimeField(auto_now_add=True)
  author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
