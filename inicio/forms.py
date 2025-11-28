from django import forms
from .models import Articulo

class FormularioArticulo(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ['tipo', 'marca', 'stock', 'imagen']

        widgets = {
            'tipo': forms.TextInput(attrs={'class': 'form-control'}),
            'marca': forms.TextInput(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

