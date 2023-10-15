from django.urls import path
from inicio.views import inicio, create_alias, listado_alias, edit_alias,delete_alias,detalle_alias, mostrar_tweets
from . import views

urlpatterns = [
    path('', inicio, name='inicio'),
    # path('create-alias/<str:alias>/<int:followers>', create_alias, name='create_alias'),
    path('alias/', listado_alias, name='alias'),
    path('alias/create/', create_alias, name='create_alias'),
    path('alias/<int:alias_id>/edit/', edit_alias, name='edit_alias'),
    path('alias/<int:alias_id>/', detalle_alias, name='detalle_alias'),
    path('alias/<int:alias_id>/delete/', delete_alias, name='delete_alias'),
    path('tweet/create/', views.create_tweet, name='create_tweet'),
    path('tweets/', mostrar_tweets, name='mostrar_tweets'),
    
]
