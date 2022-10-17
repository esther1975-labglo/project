from Assignment.models import students, mark, course
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import studentform, markform
from django.http import JsonResponse
import json
from django.core.serializers import serialize
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages


def home(request):
    return render (request,'home.html')

def user_login(request): 
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request,user)
            return redirect('/Assignment/listview')
        else:
            messages.error(request, 'invalid')
            return redirect('login')
    else:     
        form = AuthenticationForm()
        return render(request,'login.html',{'form':form})
        
def user_logout(request):
    logout(request)
    return redirect('/Assignment')
   
def jsondata(request):
 	form = students.objects.all()
 	data = serialize("json", form)
 	data = json.loads(data)
 	return JsonResponse(data, status = 200, safe = False) # any object can be passed for serialization, otherwise only dict instances are allowed

def jsondetails(request):
    form = students.objects.all()
    data = serialize("json", form)
    data = json.loads(data)
    return JsonResponse(data, status = 200, safe = False)	
 	
def json_data(request):
	data = students.objects.all()
	obj = json.loads(data)
	return HttpResponse(request, {"obj":obj})
	

def add(request):
    get = studentform(request.POST or None, request.FILES or None)
    if get.is_valid():
       get = get.save(commit = False)
       get.created_by = (request.user).username
       get.save()
    else:
        pass
    return render(request,"stform.html",{'form':get})
    
def addmarks(request):
    obj = markform(request.POST or None, request.FILES or None)
    if obj.is_valid():
    	
    	obj.save()
    else:
        pass
    return render(request,"markadd.html",{'obj':obj})
    
def listview(request):
    datas = students.objects.all()
    print (datas)
    context={'datas':datas}
    return render(request, "listview.html", context)

def markview(request):
    data = mark.objects.all()
    print (data)
    context={'data':data}
    return render(request, "markview.html", context)
       
def viewdetails(request,id):
    datas = mark.objects.get(id = id)
    context={'datas':datas}
    return render(request, "marksheet.html", context)
    
def edit(request, id):
    obj = students.objects.get(id = id)
    form = markform(request.POST or None, instance = obj)
    if form.is_valid():
        form = form.save(commit = False)
        form.modified_by = (request.user).username
        form.save()
    context={'form': form}
    return render(request, "edit.html", context)

def stu_delete(request):
    obj = students.objects.get(id = id)
    form = studentform(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
    context={'form': form}
    return render(request, "delete.html", context)

    
def delete(request, id):
    obj = students.objects.get(id = id)
    form = markform(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
    context={'form': form}
    return render(request, "delete.html", context)
        
    

