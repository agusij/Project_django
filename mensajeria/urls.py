from django.urls import path
from . import views

urlpatterns = [
    path('enviar/', views.enviar_mensaje, name='enviar_mensaje'),
    path('lista/', views.lista_mensajes, name='lista_mensajes'),
    path('eliminar/<int:mensaje_id>/', views.eliminar_mensaje, name='eliminar_mensaje'),

]
