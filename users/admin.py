from django.contrib import admin

# Register your models here.
from .models import User, StdCustomer, StdVendor, University

admin.site.register(User)
admin.site.register(StdCustomer)
admin.site.register(StdVendor)
admin.site.register(University)