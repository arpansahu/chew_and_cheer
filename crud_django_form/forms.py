from django import forms
from crud_django_form.models import Item


class ItemCreation(forms.ModelForm):
    """
    Form for creating and updating menu items with enhanced styling.
    """
    class Meta:
        model = Item
        fields = ['name', 'description', 'price']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter item name (e.g., Burger, Pizza)',
                'required': True,
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter item description',
                'rows': 3,
                'required': True,
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter price (e.g., 12.99)',
                'step': '0.01',
                'min': '0',
                'required': True,
            }),
        }
        labels = {
            'name': 'Item Name',
            'description': 'Description',
            'price': 'Price ($)',
        }
        help_texts = {
            'name': 'Enter a unique name for the menu item',
            'description': 'Provide a brief description of the item',
            'price': 'Enter the price in USD',
        }

    def clean_name(self):
        """Validate and clean the name field."""
        name = self.cleaned_data.get('name')
        if name:
            name = name.strip().title()
            if len(name) < 2:
                raise forms.ValidationError('Item name must be at least 2 characters long.')
        return name

    def clean_price(self):
        """Validate the price field."""
        price = self.cleaned_data.get('price')
        if price is not None and price < 0:
            raise forms.ValidationError('Price cannot be negative.')
        if price is not None and price > 10000:
            raise forms.ValidationError('Price cannot exceed $10,000.')
        return price
