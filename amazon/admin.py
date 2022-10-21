from django.contrib import admin

from .models import product, cart, cartitem

class productadmin(admin.ModelAdmin):
    list_display = ('id','product', 'title', 'image', 'brand', 'price', 'stock_availability' )
admin.site.register(product, productadmin)

class cartadmin(admin.ModelAdmin):
    list_display = ('id', 'created_at')
admin.site.register(cart, cartadmin)

class cartitemadmin(admin.ModelAdmin):
    list_display = ('id', 'quantity', 'price')
admin.site.register(cartitem, cartitemadmin)

