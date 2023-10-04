from django.db import models

# Create your models here.

class Alias(models.Model):
    alias = models.CharField(max_length=50)
    followers = models.IntegerField()
    
    def __str__(self) -> str:
        return f'{self.alias} {self.followers}'
    
    
class Tweet(models.Model):
    content = models.TextField(max_length=140)
    createt_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # def __str__(self):
    #     return self.content[:50]
    
    # class Meta:
    #     ordering = ['-created_at']