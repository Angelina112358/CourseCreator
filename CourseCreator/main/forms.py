from .models import *
from django.forms import ModelForm, TextInput, Textarea
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class ProductForm(ModelForm):
    class Meta:
        model = Product
        exclude = ['author']
        fields = ['category', 'slug', 'name', 'description', 'price', 'stock']
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


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
