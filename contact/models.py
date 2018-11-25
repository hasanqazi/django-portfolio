from django.db import models

# Create your models here.
class ShowContact(models.Model):
  email = models.CharField(max_length=100)
  subject = models.CharField(max_length=60)
  body = models.TextField()
