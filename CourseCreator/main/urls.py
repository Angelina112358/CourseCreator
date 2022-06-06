from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('creator/', views.creator, name='creator'),
    path('catalog/', views.product_list, name='product_list'),
    path('<int:id>/<str:slug>', views.product_detail, name='product_detail'),
    path('<str:category_slug>', views.product_list, name='product_list_by_category'),
]