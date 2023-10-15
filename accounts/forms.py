from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django import forms
from django.contrib.auth.models import User


class PersonalProfile(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label = 'Password', widget= forms.PasswordInput())
    password2 = forms.CharField(label = 'Validate Password', widget= forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username' , 'email' , 'password1', 'password2']
        help_texts = {campo: '' for campo in fields}
        
class MyOwnEditProfileForm(UserChangeForm):
    password = None
    email = forms.EmailField(label='New email')
    first_name = forms.CharField(label= 'New name', max_length=30)
    last_name = forms.CharField(label= 'New surname', max_length=50)
    link = forms.URLField(required=False)
    avatar = forms.ImageField(required=False)
    
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name' , 'link']
        
    
class PersonalChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='Old password', widget=forms.PasswordInput())
    new_password1 = forms.CharField(label='New password', widget=forms.PasswordInput())
    new_password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']
