from django import forms

from .models import Catalogue

class AddCatalogueForm(forms.ModelForm):
    class Meta:
        model = Catalogue
        fields = "__all__"

        widgets = {
            'title': forms.fields.TextInput(attrs={
                'class': 'form-control'
            }),
            'ISBN': forms.fields.TextInput(attrs={
                'class': 'form-control'
            }),
            'author': forms.fields.TextInput(attrs={
                'class': 'form-control'
            }),
            'price': forms.fields.NumberInput(attrs={
                'class': 'form-control'
            }),
            'availability': forms.fields.Select(attrs={
                'class': 'form-control'
            })
        }