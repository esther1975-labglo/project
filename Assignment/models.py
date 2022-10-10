from django.db import models

class students(models.Model):
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=30,null = True)
    img = models.ImageField(upload_to="images/")
    created_time = models.DateTimeField(auto_now = True)
    updated_time = models.DateTimeField(auto_now_add = True)
    created_by = models.CharField(max_length = 50)
    modified_by = models.CharField(max_length = 50)
    def __str__(self):
        return "{} {} {} {} {} {} {}".format(self.first_name, self.last_name, self.img, self.created_time, self.updated_time, self.created_by, self.modified_by)

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
      



