from django.db import models
import datetime
from django.db.models import CASCADE
from django.utils.crypto import get_random_string


def new_file_name(instance, filename):
    return 'files/{0}{1}'.format(get_random_string(length=10), filename)

def new_image_name(instance, filename):
    return 'images/{0}{1}'.format(get_random_string(length=10), imagename)

class Categories(models.Model):
    name = models.CharField(max_length = 20)
    created = models.DateTimeField(auto_now = True)
    updated = models.DateTimeField(auto_now = True)
    status = models.BooleanField()
    def __str__(self):
        return "%d " % (self.id)

class Items(models.Model):

    name = models.CharField(max_length = 20)
    files = models.FileField(upload_to=new_file_name,
                              blank=True,
                              null=True)
    images = models.ImageField(upload_to=new_image_name,
                              blank=True,
                              null=True)
    descrip = models.TextField(max_length = 200)
    price = models.DecimalField(max_digits= 7,decimal_places= 2)
    status = models.BooleanField()
    created = models.DateTimeField(auto_now = True)
    updated = models.DateTimeField(auto_now = True)
    categorie= models.ForeignKey(Categories,on_delete = models.CASCADE,default = None)


    def __str__(self):
        return "%d " % (self.id)




class Users(models.Model):
    name = models.CharField(max_length = 20)
    address = models.TextField(max_length = 80)
    mobile = models.CharField(max_length = 10)
    email = models.CharField(max_length = 20,default = None)
    created = models.DateTimeField(auto_now = True)
    updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return " %d " % (self.id)


class Orders(models.Model):
    user = models.ForeignKey(Users,on_delete = models.CASCADE)
    item = models.ForeignKey(Items,on_delete = models.CASCADE)
    categories= models.ForeignKey(Categories,on_delete = models.CASCADE)
    STATUS_CHOICES = (
           (1, 'in cart'),
           (2, 'purchased'),)
    status  = models.IntegerField(choices = STATUS_CHOICES)
    total_price = models.IntegerField()
    created = models.DateTimeField(auto_now = True)
    updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return " %d " % (self.id)
