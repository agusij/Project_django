from django.shortcuts import render, redirect
from django.template import Template, Context, loader
from django.http import HttpResponse
from datetime import datetime
from inicio.models import Alias
from inicio.forms import AliasFormulario, AliasBusquedaFormulario, CrearAliasForlmulario, EditarAliasForlmulario
from django.contrib.auth.decorators import login_required





def inicio (request):
    
    datos = {
        'fecha': datetime.now()
        
    }
    
  

    return render(request, r'inicio/inicio.html', datos)




def create_alias(request):
   
   if request.method == 'POST':
        formulario = AliasFormulario(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            alias = Alias(alias=data.get('alias') , followers=data['followers'])
            alias.save()
            return redirect('alias')
            
        else:
            return render(request, r'inicio/create_alias.html', {'formulario' : formulario})
   
   formulario = AliasFormulario()
   return render(request, r'inicio/create_alias.html', {'formulario' : formulario})




@login_required
def edit_alias(request, alias_id):
    alias_a_editar = Alias.objects.get(id=alias_id)
    
    if request.method == 'POST':
        formulario = EditarAliasForlmulario(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            alias_a_editar.alias = data['alias']
            alias_a_editar.followers = data['followers']
            alias_a_editar.save()
            return redirect('alias')
            
        else:
            return render (request, 'inicio/edit_alias.html', {'formulario': formulario})
    
    formulario = EditarAliasForlmulario(initial={'alias': alias_a_editar.alias, 'followers': alias_a_editar.followers})
    return render(request, r'inicio/edit_alias.html', {'formulario': formulario})


def listado_alias(request):
    if request.method == 'GET' and 'alias' in request.GET:
        form = AliasBusquedaFormulario(request.GET)
        if form.is_valid():
            alias_encontrados = Alias.objects.filter(alias__icontains=form.cleaned_data['alias'])
        else:
            alias_encontrados = []
    else:
        form = AliasBusquedaFormulario()
        alias_encontrados = Alias.objects.all()
    return render(request, r'inicio/listado_alias.html' , {'formulario': form, 'alias_encontrados': alias_encontrados})

@login_required
def delete_alias(request, alias_id):
    alias_a_aliminar = Alias.objects.get(id=alias_id)
    alias_a_aliminar.delete()
    
    
    return redirect('alias')

def detalle_alias(request, alias_id):
    alias = Alias.objects.get(id=alias_id)
    return render(request, 'inicio/detalle_alias.html' , {'alias' : alias})


def about_me(request):
    return render(request, 'inicio/about_me.html')
