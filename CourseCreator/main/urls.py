from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('catalog/', views.product_list, name='catalog'),
    path('product/', views.product_detail, name='product'),
]