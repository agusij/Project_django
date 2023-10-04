from django.shortcuts import render
from django.template import Template, Context, loader
from django.http import HttpResponse
from datetime import datetime
from inicio.models import Alias
from inicio.forms import AliasFormulario, AliasBusquedaFormulario

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


# def create_alias(request, alias , followers):
   
#    alias = Alias(alias=alias , followers=followers)
#    alias.save()
   
#    return render(request, r'inicio/new_alias.html', {})


def create_alias(request):
   
   if request.method == 'POST':
        formulario = AliasFormulario(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            alias = Alias(alias=data.get('alias') , followers=data['followers'])
            alias.save()
            
        else:
            return render(request, r'inicio/create_alias.html', {'formulario' : formulario})
   
   formulario = AliasFormulario()
   return render(request, r'inicio/create_alias.html', {'formulario' : formulario})



def listado_alias(request):
    
    formulario = AliasBusquedaFormulario(request.GET)
    if formulario.is_valid():
            alias_a_buscar = formulario.cleaned_data.get('alias')
            alias_encontrados = Alias.objects.filter(alias__icontains=alias_a_buscar)
            
            
            
    else:
        alias_encontrados = Alias.objects.all()
   
    formulario = AliasBusquedaFormulario()
    return render(request, r'inicio/listado_alias.html', {'formulario' : formulario, 'alias_encontrados': alias_encontrados})