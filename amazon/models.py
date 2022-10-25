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
#second try

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10, null=True, blank=True)
 
    def __str__(self):
        return self.name
 
class things(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    price = models.FloatField()
    image = models.ImageField(upload_to="images", default="")
 
    def __str__(self):
        return self.name
 
class Feature(models.Model):
    product = models.ForeignKey(things, on_delete=models.CASCADE)
    feature = models.CharField(max_length=1000, null=True, blank=True)
 
    def __str__(self):
        return str(self.product) + " Feature: " + self.feature
 
class Review(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE) 
    product = models.ForeignKey(things, on_delete=models.CASCADE)
    content = models.TextField()
    datetime = models.DateTimeField()  
 
    def __str__(self):
        return str(self.customer) +  " Review: " + self.content
 
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100)
 
    def __str__(self):
        return str(self.id)
 
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
 
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total
 
class OrderItem(models.Model):
    product = models.ForeignKey(things, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(null = True)
 
    def __str__(self):
        return str(self.order)
 
    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total
 
class CheckoutDetail(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    total_amount = models.CharField(max_length=10, blank=True,null=True)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return self.address   