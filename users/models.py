from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# Create your models here.


class User(AbstractUser):
    school_email = models.EmailField(max_length=255)
    reg_no = models.CharField(max_length=255, unique=True)
    is_customer = models.BooleanField(default=False)
    is_vendor = models.BooleanField(default=False)

    # USERNAME_FIELD = ['reg_no']
    # REQUIRED_FIELDS = []

    # objects = models.Manager()

    def get_school_email(self):
        return self.school_email
    
    def get_reg_no(self):
        return self.reg_no


class University(models.Model):
    uni_name = models.CharField(max_length=255)
    uni_address = models.CharField(max_length=255)

    def __str__(self):
        return self.uni_name

class StdCustomer(models.Model):
    student = models.OneToOneField(User, on_delete=models.CASCADE)
    st_uni = models.ForeignKey(University, on_delete=models.CASCADE)
    address  = models.CharField(max_length=255, blank=True)
    bio = models.TextField(blank=True, null=True)
    profile = models.ImageField(default='default.jpg', upload_to='profiles')
    dob = models.DateField(max_length=15)
    phone_number = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def register(self):
        self.save()
    
    @staticmethod
    def get_stdcustomer_by_reg_no(reg_no):
        try:
            return StdCustomer.objects.get(reg_no=reg_no)
        except:
            return False
        
    def isExists(self):
        if StdCustomer.objects.filter(reg_no = self.reg_no):
            return True
        return False

    def __str__(self):
        return self.student.username
    
class StdVendor(StdCustomer):
    pass
