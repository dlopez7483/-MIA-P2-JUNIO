from django import forms


class PrincipalForm(forms.Form):
    archivo = forms.FileField(required=False)
    consola_entrada  = forms.CharField(required=False, widget=forms.Textarea)
    #consola_salida  = forms.CharField(widget=forms.Textarea)