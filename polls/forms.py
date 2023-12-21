from django import forms
from .models import darcek

class darcekform(forms.ModelForm):
    class Meta:
        model = darcek
        fields = ['nazov', 'link', 'pre', 'cena' ]