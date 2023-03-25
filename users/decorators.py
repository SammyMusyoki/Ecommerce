from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test

def customer_required(function=None, redirect_field_name = REDIRECT_FIELD_NAME, login_url = 'login'):
    '''
    Decorators for views that checks that the logged in user is a customer.
    '''
    actual_decorator = user_passes_test(
        lambda u: u.is_authenticated and u.is_customer,
        login_url=login_url,
        redirect_field_name=redirect_field_name,
    )
    if function:
        actual_decorator(function)
    return actual_decorator

def vendor_required(function=None, redirect_field_name = REDIRECT_FIELD_NAME, login_url = 'login'):
    '''
    Decorators for views that checks that the logged in user is a customer.
    '''
    actual_decorator = user_passes_test(
        lambda u: u.is_authenticated and u.is_vendor,
        login_url=login_url,
        redirect_field_name=redirect_field_name,
    )
    if function:
        actual_decorator(function)
    return actual_decorator