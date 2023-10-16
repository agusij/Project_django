from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField


class Tweet(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = RichTextField(blank=True, null=True, max_length=280)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content[:50] + "..."
    
    class Meta:
        ordering = ['-created_at']