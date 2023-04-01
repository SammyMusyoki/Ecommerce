from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('vendor-shop/<str:id>', views.vendor_dashboard, name='vendor-dashboard'),

    path('product/create-product/', views.create_product, name='create-product'),
    path('product/update-product/<str:id>/', views.update_product, name='update-product'),
    path('product/delete-product/<str:id>/', views.delete_product, name='delete-product'),
]