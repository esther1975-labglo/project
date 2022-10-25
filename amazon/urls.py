from django.urls import path
from amazon import views
from django.contrib import admin
from .views import SearchResultsView, SearchView, Productlist, Product_list 


urlpatterns = [	path("productview/", views.listview, name = "productview"),
                path("dynamic/productview/", views.dynamic_product_view, name = "dynamic_product_view"),
                path("searched/productview/", views.search_box, name = "search_box"),
                path("search/", SearchResultsView.as_view(), name="search_results"),
                path("searchview/", SearchView.as_view(), name="search_view"),
                path("ProductList/", Productlist.as_view(), name="ProductList"),
              
               
                #second try

                path("", views.index, name="index"),
                path("Cart/", views.cart, name="cart"),
                path("Product_list/", Product_list.as_view(), name="Product_list"),
                path("checkout/", views.checkout, name="checkout"),
                #path("update_item/", views.updateItem, name="update_item"),
                path("product_view/<int:myid>/", views.product_view, name="product_view"),
                path("Searching_product/", views.search, name="search"),
                path("contact/", views.contact, name="contact"),
                path("tracking/", views.tracker, name="tracker"),
                #path("loggedin_contact/", views.loggedin_contact, name="loggedin_contact"),
 
                #path("register/", views.register, name="register"),
                path("change_password/", views.change_password, name="change_password"),
                #path("login/", views.Login, name="login"),
                #path("logout/", views.Logout, name="logout"),
#
                ]
				