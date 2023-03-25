from django import forms
from django.contrib.auth.forms import UserCreationForm
from shop.models import Shop
from .models import User
from django.db import transaction

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    student_email = forms.EmailField(required=True)
    reg_no = forms.CharField(max_length=15, required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'student_email', 'reg_no', 'password1', 'password2']

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.save()
        return user
    
class VendorSignUpForm(forms.ModelForm):

    class Meta:
        model = Shop
        fields = ['shop_name', 'shop_address', 'shop_phone']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_vendor = True
        if commit:
            user.save()
        return user