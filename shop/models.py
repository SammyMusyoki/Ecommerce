from django.db import models
from users.models import User,StdVendor
import datetime

# Create your models here.

class Shop(models.Model):
    shop_owner = models.ForeignKey(StdVendor,on_delete=models.CASCADE)
    shop_name = models.CharField(max_length=255, unique=True, blank=False)
    shop_address = models.CharField(max_length=255, blank=False)
    shop_phone = models.CharField(max_length=255, blank=False)
    shop_banner = models.ImageField(default='default.jpg', upload_to='shop-banners')
    shop_profile = models.ImageField(default='default.jpg', upload_to='shop-profiles')

    def __str__(self):
        return self.shop_name
    
class Category(models.Model):
    name = models.CharField(max_length=50)

    @staticmethod
    def get_all_categories():
        return Category.objects.all()
    
    def __str__(self):
        return self.name
    
class Products(models.Model):
    name = models.CharField(max_length=60)
    product_shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=255, default='', blank=True, null=True)
    image = models.ImageField(upload_to='products/images/')

    @staticmethod
    def get_products_by_id(ids):
        return Products.objects.filter(id__in=ids)
    
    @staticmethod
    def get_all_products():
        return Products.objects.all()
    
    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Products.objects.filter(category=category_id)
        else:
            return Products.get_all_products()

class Order(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=50, default='', blank=True)
    phone = models.CharField(max_length=50, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)
    
    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')