from django.contrib import admin
from inicio.models import Alias
from .models import Tweet
# Register your models here.

admin.site.register(Alias)
admin.site.register(Tweet)