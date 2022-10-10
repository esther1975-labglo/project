from django import forms 
from Assignment.models import students, mark
  
class studentform(forms.ModelForm):  
    class Meta:  
        model = students  
        fields = ["id","first_name","last_name","img"]
        name = forms.CharField()
        schoolapp_field = forms.ImageField()
        
        def save(self, commit = True):
        	 user = super(studentform, self).save(commit = False)
        	 if commit:
        	 	user.save()
        	 return user	

class markform(forms.ModelForm):  
    class Meta:  
        model = mark 
        fields = ["stu_id", "subject", "mark"]
