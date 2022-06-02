from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('catalog/', views.product_list, name='catalog'),
]