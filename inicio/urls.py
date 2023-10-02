from django.urls import path
from inicio.views import inicio, create_alias

urlpatterns = [
    path('', inicio),
    path('create-alias/<str:alias>/<int:followers>', create_alias),
]
