# bordados/forms.py

from django import forms
from .models import Bordado

class BordadoForm(forms.ModelForm):
    class Meta:
        model = Bordado
        fields = ['Nome', 'Tamanho', 'Status', 'Quantidade','Telefone']
