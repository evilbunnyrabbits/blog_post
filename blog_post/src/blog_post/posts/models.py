from django.db import models
from django.conf import settings

# Create your models here.
class Post(models.Model):
    title = models.TextField()
    content = models.TextField()