from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login as django_login
from accounts.forms import PersonalProfile, MyOwnEditProfileForm, PersonalChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy

def login(request):
    
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)    
        if formulario.is_valid():
            username = formulario.cleaned_data.get('username')
            password = formulario.cleaned_data.get('password')
            
            usuario = authenticate(username=username , password=password)
            
            django_login(request, usuario)
            
            return redirect('inicio')
        
    else:
    
        formulario = AuthenticationForm()
    
    return render(request, 'accounts/login.html', {'formulario': formulario})


def register(request):
    
    if request.method == 'POST':
            formulario= PersonalProfile(request.POST)
            if formulario.is_valid():
                formulario.save()
                return redirect ('login')
    
    else:
            formulario = PersonalProfile()
    return render(request, 'accounts/register.html', {'formulario': formulario})


def edit_profile(request):
    
    if request.method =='POST':
        formulario = MyOwnEditProfileForm(request.POST , instance=request.user)
        if formulario.is_valid():
            formulario.save()
            return redirect('inicio') #mandar al perfil cuando se cree
        
    else:
    
     formulario= MyOwnEditProfileForm(instance=request.user)
    return render(request, 'accounts/edit_profile.html', {'formulario': formulario})


class ChangePassword(PasswordChangeView):
    template_name = 'accounts/edit_pass.html'
    form_class = PersonalChangeForm
    success_url = reverse_lazy('edit_profile')