from django.urls import path
from inicio.views import inicio, create_alias

urlpatterns = [
    path('', inicio, name='inicio'),
    # path('create-alias/<str:alias>/<int:followers>', create_alias, name='create_alias'),
    path('alias/create/', create_alias, name='create_alias')
    
]
