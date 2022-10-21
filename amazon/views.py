from amazon.models import product, cart, cartitem
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from amazon.forms import productform
from django.views.generic.list import ListView
from django.db.models import Q
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView


def listview(request):
    datas = product.objects.all()
    print (datas)
    find = product.objects.filter(title__icontains = request.GET.get('search'))
    context={'datas':datas, 'find':find}
    
    return render(request, "product_view.html", context)

def search_box(request):
    product_QS = request.GET.get("product_QS")
    if product_QS is None:
	    product_QS = "iphone"
    else:
        mydict = product.objects.get(title = product_QS)
        return render(request,"product_view.html")	
    return render(request,"product_view.html")

class SearchResultsView(ListView):
    model = product
    template_name = 'search_results.html'

    

    def search_box(request):
        product_QS = request.GET.get("product_QS")
        if product_QS is None:
	        product_QS = "iphone"
        else:
            mydict = product.objects.get(title = product_QS)
            return render(request,"product_view.html")	
        return render(request,"product_view.html")

    def get_queryset(self): # new
        #context['datas'] = product.objects.filter(title__icontains = request.GET.get('search'))
        #return render(request, "product_view.html", context)
        return product.objects.filter(title__icontains = 'iphone')

class SearchView(ListView):
    model = product
    template_name = 'search.html'
   
    def get_queryset(self):
       result = super(SearchView, self).get_queryset()
       query = self.request.GET.get('search')
       if query:
          postresult = product.objects.filter(title__contains = query)
          result = postresult
       else:
           result = None
       return result

def dynamic_product_view(request):
    context['datas'] = product.objects.filter(title__icontains = request.GET.get('search'))
    return render(request, "dynamic_product_view.html", context)   

class ProductList(ListView):
    model = product
    template_name = 'productList.html'
    
    def get_queryset(self):
        
        queryset = product.objects.all()
        if self.request.GET.keys():
           if self.request.GET.get('src') != '':
                keyword = self.request.GET.get('src')
                queryset = product.objects.filter(Q(title = keyword.capitalize()) | Q(title = keyword.capitalize()))
        return queryset

class DetailCart(DetailView):
    model = cart
    template_name='cart/detail_cart.html'

class ListCart(ListView):
    model = cart
    template_name='list_cart.html'

class CreateCart(CreateView):
    model = cart
    template_name = 'create_cart.html'

class Updatecart(UpdateView):
    model = cart
    template_name = 'update_cart.html'

class DeleteCart(DeleteView):
    model = cart
    template_name = 'delete_cart.html'

class DetailCartItem(DetailView):
    model = cartitem
    template_name='detail_cartitem.html'

class ListCartItem(ListView):
    model = cartitem
    template_name='list_cartitems.html'

class CreateCartItem(CreateView):
    model = cartitem
    template_name = 'create_cartitem.html'

class UpdateCartItem(UpdateView):
    model = cartitem
    template_name = 'update_cartitem.html'

class DeleteCartItem(DeleteView):
    model = cart
    template_name = 'delete_cartitem.html'
                
    
