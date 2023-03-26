from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('vendor-shop/<str:id>', views.vendor_shop, name='vendor-shop'),
    path('create-product/', views.create_product, name='create-product'),
    path('update-product/<str:id>/', views.update_product, name='update-product'),
]