from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login as django_login
from accounts.forms import PersonalProfile, MyOwnEditProfileForm, PersonalChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import ExtraInfo

def login(request):
    
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)    
        if formulario.is_valid():
            username = formulario.cleaned_data.get('username')
            password = formulario.cleaned_data.get('password')
            
            usuario = authenticate(username=username , password=password)
            
            django_login(request, usuario)
            
            ExtraInfo.objects.get_or_create(user=usuario)
            
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

@login_required
def edit_profile(request):
    extra_info = request.user.extrainfo
    if request.method == 'POST':
        formulario = MyOwnEditProfileForm(request.POST, request.FILES, instance=request.user)
        if formulario.is_valid():
            user = formulario.save()
            
            extra_info.link = formulario.cleaned_data.get('link')
            if formulario.cleaned_data.get('avatar'):
                extra_info.avatar = formulario.cleaned_data.get('avatar')
            extra_info.save()
            
            return redirect('profile')
    else:
        formulario = MyOwnEditProfileForm(
            initial={'link': extra_info.link, 'avatar': extra_info.avatar},
            instance=request.user
        )
    return render(request, 'accounts/edit_profile.html', {'formulario': formulario})



class ChangePassword(LoginRequiredMixin, PasswordChangeView):
    template_name = 'accounts/edit_pass.html'
    form_class = PersonalChangeForm
    success_url = reverse_lazy('edit_profile')
    
@login_required    
def profile(request):
    user = request.user
    extra_info, created  = ExtraInfo.objects.get_or_create(user=user)
    
    context = {
       'user': user,
       'extra_info': extra_info 
        
    }
    
    return render(request, 'accounts/profile.html', context)