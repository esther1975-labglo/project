from django.urls import path
from amazon import views
from django.contrib import admin
from .views import SearchResultsView, SearchView, ProductList, ListCart, DetailCart, CreateCart,  Updatecart, DeleteCart
from .views import ListCartItem, DetailCartItem, CreateCartItem, UpdateCartItem, DeleteCartItem

urlpatterns = [	path("productview/", views.listview, name = "productview"),
                path("dynamic/productview/", views.dynamic_product_view, name = "dynamic_product_view"),
                path("searched/productview/", views.search_box, name = "search_box"),
                path("search/", SearchResultsView.as_view(), name="search_results"),
                path("searchview/", SearchView.as_view(), name="search_view"),
                path("ProductList/", ProductList.as_view(), name="ProductList"),
                path('cart/', ListCart.as_view, name='list-carts'),
                path('cart/<int:pk>/',DetailCart.as_view(), name='detail-cart'),
                path('cart/create/', CreateCart.as_view(), name='create-cart'),
                path('cart/<int:pk>/update/', Updatecart.as_view(), name='update-cart'),
                path('cart/<int:pk>/delete/', DeleteCart.as_view(), name='delete-cart'),
                path('cartitem/', ListCartItem.as_view(), name='list-cartitem'),
                path('cartitem/<int:pk>/', DetailCartItem.as_view(), name='detail-cartitem'),
                path('cartitem/create/', CreateCartItem.as_view(), name='create-cartitem'),
                path('cartitem/<int:pk>/update/', UpdateCartItem.as_view(), name='update-cartitem'),
                path('cartitem/<int:pk>/delete/', DeleteCartItem.as_view(), name='delete-cartitem'),
]
				