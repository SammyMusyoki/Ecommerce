from django import forms
from .models import Products

class CreateProductForm(forms.ModelForm):
    
    class Meta:
        model = Products
        fields = ['name', 'description', 'price', 'category', 'image']


class UpdateProductForm(forms.ModelForm):

    class Meta:
        model = Products
        fields = ['name', 'description', 'price', 'category', 'image']