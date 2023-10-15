from django import forms
from .models import Tweet

class AliasFormulario(forms.Form):
    alias = forms.CharField(max_length=50)
    followers = forms.IntegerField()
    
    
class EditarAliasForlmulario(AliasFormulario):
    ...
       
class CrearAliasForlmulario(AliasFormulario):
    ...
       
    

class AliasBusquedaFormulario(forms.Form):
    alias = forms.CharField(max_length=50 , required=False)
    
    
class TweetForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
    'rows': 4, 
    'cols': 50, 
    'class': 'mi-clase-css',
    'placeholder': 'Escribe tu tweet aquí...'
}))

    
    class Meta:
        model = Tweet
        fields = ['content']
