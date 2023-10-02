from django.db import models

# Create your models here.

class UserProfile(models.Model):
    alias = models.CharField(max_length=50)
    followers = models.IntegerField()