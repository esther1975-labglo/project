from django import forms 
from amazon.models import product
  
class productform(forms.ModelForm):  
    class Meta:  
        model = product  
        fields = ["id","product", "title", "image", "brand", "price", "stock_availability"]
        
        
        	