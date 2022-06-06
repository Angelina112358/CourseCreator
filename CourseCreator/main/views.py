from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product
from .forms import ProductForm


def index(request):
    return render(request, 'main/index.html')


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'main/catalog.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    return render(request,
                  'main/product.html',
                  {'product': product})


def creator(request):
    error = ''
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('home')
        else:
            error = 'Неверная форма'
    form = ProductForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/creator.html', context)


