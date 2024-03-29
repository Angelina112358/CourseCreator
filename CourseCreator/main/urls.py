from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='home'),
    path('creator/', views.Creator.as_view(), name='creator'),
    path('creator_done', views.Creator.as_view(), name='creator_done'),
    path('catalog/', views.ProductList.as_view(), name='product_list'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout', views.LogOutView.as_view(), name='logout'),
    path('register', views.RegisterView.as_view(), name='register'),
    path('<int:id>/delete/', views.delete_view, name='delete'),
    path('catalog/<int:id>/delete', views.delete_view, name='delete'),
    path('<int:id>/edit', views.update_view, name='edit'),
    path('catalog/<int:id>/edit', views.update_view, name='edit'),
    path('<int:id>/<str:slug>', views.ProductDetail.as_view(), name='product_detail'),
    path('<str:category_slug>', views.ProductList.as_view(), name='product_list_by_category'),

]
