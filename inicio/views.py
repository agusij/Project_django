from django.shortcuts import render
from django.template import Template, Context, loader
from django.http import HttpResponse
from datetime import datetime
from inicio.models import UserProfile

# Create your views here.

def inicio (request):
    
    datos = {
        'fecha': datetime.now()
        
    }
    
    #V1
    # archivo = open(r'inicio/templates/inicio/inicio.html', 'r')
    # template = Template(archivo.read())
    # contexto = Context(datos)
    # template_renderizado = template.render(contexto)
    # return HttpResponse(template_renderizado)



 #V2
    # template = loader.get_template(r'inicio/inicio.html')
    # template_renderizado = template.render(datos)
    # return HttpResponse(template_renderizado)


## v3

    return render(request, r'inicio/inicio.html', datos)


def create_alias(request, alias , followers):
   
   alias = UserProfile(alias=alias , followers=followers)
   alias.save()
   
   return render(request, r'inicio/new_alias.html', {})