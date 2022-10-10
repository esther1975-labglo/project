from django.urls import path
from Assignment import views
from django.contrib import admin

urlpatterns = [ path("", views.home, name="home"),
              path("login/", views.user_login, name = "login"),
              path("logout/",views.user_logout, name = "logout"),
              path('add',views.add,  name = "add"),
	      path('addmarks/',views.addmarks,  name = "addmarks"),
	      path('viewdetails/<int:id>',views.viewdetails,  name = "viewdetails"),
	      path('listview',views.listview,  name = "listview"),
	      path('markview',views.markview,  name = "markview"),
	      path('edit/<int:id>',views.edit,  name = "edit"),
	      path('delete/<int:id>',views.delete, name = "delete"),
	      path('jsondata/',views.jsondata, name = "jsondata"),
	      path('json_data',views.json_data, name = "json_data"),
	      ]
	
