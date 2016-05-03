from django import forms
from models import Product


class NewProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'catagory', 'image', 'price')




