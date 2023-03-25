from django.contrib import admin

# Register your models here.
from .models import Shop, Category, Products, Order

class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Products, AdminProduct)
admin.site.register(Category)
admin.site.register(Shop)
admin.site.register(Order)