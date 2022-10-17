from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save, pre_delete, post_delete, pre_init, post_init
from django.utils.text import slugify
from django.utils import timezone
from django.core.mail import send_mail
from PIL import Image

class profile(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	image = models.ImageField(default = "/home/user/Pictures/Screenshots/Screenshot from 2022-09-24 17-46-16.png", upload_to = "profile_pics")
	
	def __str__(self):
		return f'{self.user.username}profile'
      
class students(models.Model):
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=30,null = True)
    slug = models.SlugField(blank = True, null = True)
    img = models.ImageField(upload_to="images/")
    created_time = models.DateTimeField(auto_now = True)
    updated_time = models.DateTimeField(auto_now_add = True)
    created_by = models.CharField(max_length = 50)
    modified_by = models.CharField(max_length = 50)
    def __str__(self):
        return "{} {} {} {} {} {} {}".format(self.first_name, self.last_name, self.img, self.created_time, self.updated_time, self.created_by, self.modified_by)
    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.first_name)
        super().save(*args, **kwargs)
        # obj.save()
def student_pre_save(sender, instance, *args, **kwargs):
    print('pre_save')
    print(sender, instance,)
    send_mail('mail', 'your student_name is now {} '.format(instance.first_name), "Don't Reply <do_not_reply@domain.example>", ['{}'.format(instance.last_name)]) 
pre_save.connect(student_pre_save, sender = students)           

def student_post_save(*args, **kwargs):
    print('post_save')  
    print(args, kwargs)
post_save.connect(student_post_save, sender = students)

def student_pre_delete(sender, instance, *args, **kwargs):
    print("pre_delete")
    print(args, kwargs)
    print("you are about to delete something!")
pre_delete.connect(student_pre_delete, sender = students)           


def student_post_delete(sender, instance, *args, **kwargs):
    print("pre_delete")
    print(args, kwargs)
    print("you have just deleted a student!")    
post_delete.connect(student_post_delete, sender = students)

def student_pre_init(sender, **kwargs):
    print('pre_init', sender, kwargs)
pre_init.connect(student_pre_init)

def student_post_init(sender, **kwargs):
    print('post_init', sender, kwargs)
post_init.connect(student_post_init)


class mark(models.Model):
	course_choices = (('1','Java'), ('2','Python'), ('3','Javascript'))
	stu_id = models.ForeignKey(students, on_delete = models.CASCADE)
	subject = models.CharField(max_length = 50,  choices = course_choices)
	mark = models.IntegerField(null = True)

	def __str__(self):
		return "{} {} {}".format(self.stu_id, self.subject, self.mark)

  
class course(models.Model):
    name = models.CharField(max_length=50)
    rollno = models.IntegerField()
    course = models.CharField(max_length=15)
      
#aggregation 

class Author(models.Model):
    name = models.CharField(max_length = 100)
    age = models.IntegerField()

class Publisher(models.Model):
    name = models.CharField(max_length = 300)
    version = models.IntegerField(null = True)

class Book(models.Model):
    name = models.CharField(max_length=300)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField()
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    pubdate = models.DateField()
    
    def __str__(self):
    	return "{} {} {} {} {} {} {}".format(self.name, self.pages, self.price,  self.rating, self.authors, self.publisher, self.pubdate)
   

class Store(models.Model):
    name = models.CharField(max_length=300)
    rating = models.FloatField(null = True)
    books = models.ManyToManyField(Book)
