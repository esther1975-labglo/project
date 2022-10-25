from django.contrib import admin

from .models import product, cart, cartitem, things, Customer, Feature, Review, Order, OrderItem, CheckoutDetail

class productadmin(admin.ModelAdmin):
    list_display = ('id','product', 'title', 'image', 'brand', 'price', 'stock_availability' )
admin.site.register(product, productadmin)

class cartadmin(admin.ModelAdmin):
    list_display = ('id', 'created_at')
admin.site.register(cart, cartadmin)

class cartitemadmin(admin.ModelAdmin):
    list_display = ('id', 'quantity', 'price')
admin.site.register(cartitem, cartitemadmin)

# second try

class thingsadmin(admin.ModelAdmin):
    list_display = ('id','title', 'name', 'price', 'image')
admin.site.register(things, thingsadmin)

class Customeradmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone_number')
admin.site.register(Customer, Customeradmin)

class Featureadmin(admin.ModelAdmin):
    list_display = ('id', 'feature')
admin.site.register(Feature, Featureadmin)

class Reviewadmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'datetime')
admin.site.register(Review, Reviewadmin)

class  Orderadmin(admin.ModelAdmin):
    list_display = ('id', 'date_ordered', 'complete', 'transaction_id')
admin.site.register(Order,  Orderadmin)

class OrderItemadmin(admin.ModelAdmin):
    list_display = ('id', 'quantity', 'date_added')
admin.site.register(OrderItem, OrderItemadmin)

class CheckoutDetailadmin(admin.ModelAdmin):
    list_display = ('id', 'phone_number', 'total_amount', 'address', 'city', 'state', 'zipcode', 'date_added')
admin.site.register(CheckoutDetail, CheckoutDetailadmin)

