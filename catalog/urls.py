from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.HomeListView.as_view(), name='home'),
    path('contacts/', views.ContactsView.as_view(), name='contacts'),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('product/create/', views.ProductCreateView.as_view(), name='create_product'),
    path('product/<int:pk>/edit/', views.ProductUpdateView.as_view(), name='edit_product'),
    path('product/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='delete_product'),
    path('product/<int:pk>/unpublish/', views.ProductUnpublishView.as_view(), name='unpublish_product'),
    path('category/<int:pk>/', views.ProductsByCategoryView.as_view(), name='products_by_category'),
]
