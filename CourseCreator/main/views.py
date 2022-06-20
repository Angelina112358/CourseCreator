from asgiref.sync import sync_to_async
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from .models import Category, Product
from .forms import ProductForm, UserForm

import asyncio


@sync_to_async
def get_product_by_id(id):
    product = Product.objects.get(id=id)
    return product


@sync_to_async
def get_all():
    categories = Category.objects.all()
    return categories


@sync_to_async
def get_filter():
    products = Product.objects.filter(available=True)
    return products


def update_view(request, id):
    context = {}

    obj = asyncio.run(get_product_by_id(id))

    form = ProductForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return render(request, "main/edit_done.html", context)

    context["form"] = form

    return render(request, "main/edit.html", context)


def delete_view(request, id):
    context = {}

    obj = asyncio.run(get_product_by_id(id))

    if request.method == "POST":
        obj.delete()
        return render(request, "main/delete_done.html", context)

    return render(request, "main/delete_view.html", context)


class Index(View):
    def get(self, request):
        return render(request, 'main/index.html')


class ProductList(View):
    def get(self, request, category_slug=None):
        category = None
        categories = asyncio.run(get_all())
        products = asyncio.run(get_filter())
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            products = products.filter(category=category)
        return render(request, 'main/catalog.html', {
            'category': category,
            'categories': categories,
            'products': products})


class ProductDetail(View):
    def get(self, request, id, slug):
        product = get_object_or_404(Product,
                                    id=id,
                                    slug=slug,
                                    available=True)
        return render(request, 'main/product.html', {'product': product})


class Creator(View):
    def get(self, request):
        if request.user.is_authenticated:
            form = ProductForm()
            context = {'form': form}
            return render(request, 'main/creator.html', context)
        else:
            return redirect('login')

    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
            response = form.save(commit=False)
            response.author = request.user
            response.save()
            return render(request, 'main/creator_done.html')
        else:
            context = {'form': form}
            return render(request, 'main/creator.html', context)


class RegisterView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            form = UserForm()
            context = {'form': form}
            return render(request, 'main/register.html', context)

    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account was successfully created for ' + username)
            return redirect('login')
        else:
            context = {'form': form}
            return render(request, 'main/register.html', context)


class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            context = {}
            return render(request, 'main/login.html', context)

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        context = {}
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'username or password is wrong')
            return render(request, 'main/login.html', context)


class LogOutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')

