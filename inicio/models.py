from django.db import models
from ckeditor.fields import RichTextField, RichTextFormField

# Create your models here.

class Alias(models.Model):
    alias = models.CharField(max_length=50)
    followers = models.IntegerField()
    
    def __str__(self) -> str:
        return f'{self.alias} {self.followers}'
    
    
class Tweet(models.Model):
    content = models.TextField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Alias, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return f"{self.content[:50]}... by {self.author.alias}" 
    
    # def __str__(self):
    #     author_name = self.author.alias if self.author else 'Unknown'
    #     return f"{self.content[:50]}... by {author_name}" 


    class Meta:
        ordering = ['-created_at']