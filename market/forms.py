# forms.py
from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['barcode', 'desc', 'r_price', 's_price', 'stock', 'unit', 'start_date', 'end_date']
        widgets = {
            # boshqa widgetlar...
            'unit': forms.Select(attrs={'class': 'form-select'}),
        }
