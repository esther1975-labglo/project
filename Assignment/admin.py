from django.contrib import admin
from .models import students, mark

class stuadmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name','img', 'created_time', 'updated_time', 'created_by', 'modified_by')
admin.site.register(students, stuadmin)

class marksdmin(admin.ModelAdmin):
    list_display = ('stu_id', 'subject', 'mark')
admin.site.register(mark, marksdmin)
# Register your models here.
