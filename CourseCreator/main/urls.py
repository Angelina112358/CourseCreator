from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('creator/', views.creator, name='creator'),
    path('catalog/', views.product_list, name='product_list'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout', views.LogOutView.as_view(), name='logout'),
    path('register', views.RegisterView.as_view(), name='register'),
    path('<int:id>/<str:slug>', views.product_detail, name='product_detail'),
    path('<str:category_slug>', views.product_list, name='product_list_by_category'),
]
