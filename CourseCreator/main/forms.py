from .models import *
from django.forms import ModelForm, TextInput, Textarea


class ProductForm(ModelForm):

    class Meta:
        model = Product
        fields = ['category', 'name', 'slug', 'description', 'price', 'stock']
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
            'stock': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Количество свободных мест',
            }),
            'slug': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Уникальный ключ',
            })
        }