from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.home, name='home'),
    path('contacts/', views.contacts, name='contacts'),
    # --- НОВОЕ: Маршрут для Задания 1 ---
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
]
