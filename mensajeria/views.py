from django.shortcuts import render, redirect
from .forms import MensajeForm
from .models import Mensaje
from django.http import HttpResponseRedirect


def enviar_mensaje(request):
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            mensaje = form.save(commit=False)
            mensaje.remitente = request.user
            mensaje.save()
            return redirect('lista_mensajes')
    else:
        form = MensajeForm()
    return render(request, 'mensajeria/enviar_mensaje.html', {'form': form})

def lista_mensajes(request):
    mensajes = Mensaje.objects.filter(destinatario=request.user)
    return render(request, 'mensajeria/lista_mensajes.html', {'mensajes': mensajes})

def eliminar_mensaje(request, mensaje_id):
    mensaje = Mensaje.objects.get(pk=mensaje_id)
    
    # Verificamos que el usuario que intenta eliminar el mensaje es el destinatario
    if request.user == mensaje.destinatario:
        mensaje.delete()
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


