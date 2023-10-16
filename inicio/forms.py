from django import forms


class AliasFormulario(forms.Form):
    alias = forms.CharField(max_length=50)
    followers = forms.IntegerField()
    
    
class EditarAliasForlmulario(AliasFormulario):
    ...
       
class CrearAliasForlmulario(AliasFormulario):
    ...
       
    

class AliasBusquedaFormulario(forms.Form):
    alias = forms.CharField(max_length=50 , required=False)
    
    

