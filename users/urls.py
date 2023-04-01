from django.urls import path
from . import views

urlpatterns = [
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/login/', views.login_user, name='login'),
    path('accounts/logout/', views.logout_user, name='logout'),

    path('accounts/pre-vendor-signup/', views.pre_vendor_signup, name='pre-vendor-signup'),
    path('accounts/vendor-signup/', views.vendor_signup, name='vendor-signup'),
]