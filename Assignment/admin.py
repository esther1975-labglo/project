from django.contrib import admin
from .models import students, mark, Author, Publisher, Book, Store

class stuadmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name','img', 'created_time', 'updated_time', 'created_by', 'modified_by')
admin.site.register(students, stuadmin)

class marksdmin(admin.ModelAdmin):
    list_display = ('stu_id', 'subject', 'mark')
admin.site.register(mark, marksdmin)

class Authoradmin(admin.ModelAdmin):
    list_display = ('name', 'age')
admin.site.register(Author, Authoradmin)

class Publisheradmin(admin.ModelAdmin):
    list_display = ('name', 'version')
admin.site.register(Publisher, Publisheradmin)

class Bookadmin(admin.ModelAdmin):
    list_display = ('name', 'pages', 'price', 'rating', 'publisher', 'pubdate')
admin.site.register(Book, Bookadmin)

class Storeadmin(admin.ModelAdmin):
    list_display = ('name', 'rating')
admin.site.register(Store, Storeadmin)
