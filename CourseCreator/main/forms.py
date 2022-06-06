from .models import *
from django.forms import ModelForm, TextInput, Textarea, ChoiceField


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'name', 'description', 'price']
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название',
            }),
            'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание',
            }),
            'price': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цена',
            }),


        }