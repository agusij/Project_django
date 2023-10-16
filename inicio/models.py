from django.db import models
from ckeditor.fields import RichTextField, RichTextFormField

# Create your models here.

class Alias(models.Model):
    alias = models.CharField(max_length=50)
    followers = models.IntegerField()
    
    def __str__(self) -> str:
        return f'{self.alias} {self.followers}'
    