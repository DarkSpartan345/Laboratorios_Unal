from django import forms
from .models import Laboratorio

class LaboratorioForm(forms.ModelForm):
    class Meta:
        model = Laboratorio
        fields = ['titulo', 'descripcion', 'objetivo', 'materiales', 'procedimiento', 'resultados', 'observaciones', 'imagen']
