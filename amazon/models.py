from django.db import models
from django.db.models import Q
from django.db.models.signals import pre_save,post_save
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
import datetime
#django.utils.timezone.now

class searchManager(models.Manager):
    def search(self, query):
        lookups = Q(title__icontains = query) | Q(brand__icontains = query)
        return self.get_queryset().filter(lookups)
        
class product(models.Model):
    product = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    slug = models.SlugField(blank = True, null = True)
    image = models.ImageField(upload_to="images/")
    brand = models.CharField(max_length=50)
    price = models.IntegerField()
    stock_availability = models.BooleanField(null = True)

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs) 

def product_pre_save(*args, **kwargs):
    print('pre_save')
    print(args, kwargs)
pre_save.connect(product_pre_save, sender = product)

def product_post_save(*args, **kwargs):
    print('post_save')
    print(args, kwargs)
post_save.connect(product_post_save, sender = product)

class cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.datetime.now())

class cartitem(models.Model):
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.FloatField(blank=True)
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)

    