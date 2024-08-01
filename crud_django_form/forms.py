from django import forms
from crud_django_form.models import Item


class ItemCreation(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description', 'price']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
        }
