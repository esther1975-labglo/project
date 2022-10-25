from amazon.models import product, cart, cartitem, things, Customer, Feature, Review, Order, OrderItem, CheckoutDetail
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

class Productlist(ListView):
    model = product
    template_name = 'productList.html'
    
    def get_queryset(self):
        
        queryset = product.objects.all()
        if self.request.GET.keys():
           if self.request.GET.get('src') != '':
                keyword = self.request.GET.get('src')
                queryset = product.objects.filter(Q(title = keyword.capitalize()) | Q(title = keyword.capitalize()))
        return queryset


                
#second try 25/10/22  
def index(request):
   #data = cartData(request)
    items = 'items'
    order = 'order'
    cartItems = 'cartItems'
 
    products = things.objects.all()
    return render(request, "index.html", {'products':products, 'cartItems':cartItems}) 
    
def search(request):
    #data = cartData(request)
    items = 'items'
    order = 'order'
    #cartItems = 'cartItems'
    if request.method == "POST":
        search = request.POST['search']
        products = things.objects.filter(name__contains=search)
        return render(request, "Search.html", {'search':search, 'products':products, 'cartItems':cartItems})
    else:
        return render(request, "Search.html")

def product_view(request, myid):
    product = things.objects.filter(id=myid).first()
    feature = Feature.objects.filter(product=product)
    reviews = Review.objects.filter(product=product)
    #data = cartData(request)
    items = 'items'
    order = 'order'
    cartItems = 'cartItems'
 
    if request.method=="POST":
        content = request.POST['content']
        review = Review(customer=customer, content=content, product=product)
        review.save()
        return redirect(f"/Product_view/{product.id}")
    return render(request, "things_view.html", {'product':product, 'cartItems':cartItems, 'feature':feature, 'reviews':reviews})

def cart(request):
    #data = cartData(request)
    items = 'items'
    order = 'order'
    cartItems = 'cartItems'
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}
    print('Cart:', cart)
 
    for i in cart:
        try:
            cartItems += cart[i]["quantity"]
 
            product = things.objects.get(id=i)
            total = (product.price * cart[i]["quantity"])
 
            order["get_cart_total"] += total
            order["get_cart_items"] += cart[i]["quantity"]
 
            item = {
                'product':{
                    'id':product.id,
                    'name':product.name,
                    'price':product.price,
                    'image':product.image,
                },
                'quantity':cart[i]["quantity"],
                'get_total':total
            }
            items.append(item)
        except:
            pass
    return render(request, "cart.html", {'items':items, 'order':order, 'cartItems':cartItems})

def cart_remove(request, item_id):
    cart_item_id = OrderItem.objects.all().last().cart_item_id
    print(cart_item_id)
    cart = Order.objects.get(cart_id=_cart_id(request))
    item = get_object_or_404(Item, id=item_id)
    cart_item = CartItem.objects.get(cart=cart, item=item, cart_item_id=cart_item_id)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()    

def checkout(request):
    #data = cartData(request)
    items = 'items'
    order = 'order'
    cartItems = 'cartItems'
    total = 'order.total'
    if request.method == "POST":
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        zipcode = request.POST['zipcode']
        phone_number = request.POST['phone_number']
        payment = request.POST['payment']
        shipping_adress = CheckoutDetail.objects.create(address=address, city=city, phone_number=phone_number, state=state, zipcode=zipcode, customer=customer, total_amount=total, order=order, payment=payment)
        shipping_adress.save()
        if total == 'order.total':
            order.complete = True
        order.save()  
        alert = True
        return render(request, "checkout.html", {'alert':alert})
    return render(request, "checkout.html", {'items':items, 'order':order, 'cartItems':cartItems})

def change_password(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    #data = cartData(request)
    items = 'items'
    order = 'order'
    cartItems = 'cartItems'
    if request.method == "POST":
        current_password = request.POST['current_password']
        new_password = request.POST['new_password']
        try:
            u = User.objects.get(id=request.user.id)
            if u.check_password(current_password):
                u.set_password(new_password)
                u.save()
                alert = True
                return render(request, "change_password.html", {'alert':alert})
            else:
                currpasswrong = True
                return render(request, "change_password.html", {'currpasswrong':currpasswrong})
        except:
            pass
    return render(request, "change_password.html", {'cartItems':cartItems})

def contact(request):
    if request.method=="POST":       
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        contact = Contact.objects.create(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        alert = True
        return render(request, 'contact.html', {'alert':alert})
    return render(request, "contact.html")

def tracker(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    #data = cartData(request)
    items = 'items'
    order = 'order'
    cartItems = 'cartItems'
    if request.method == "POST":
        order_id = request.POST['order_id']
        order = Order.objects.filter(id=order_id).first()
        order_items = OrderItem.objects.filter(order=order)
        update_order = UpdateOrder.objects.filter(order_id=order_id)
        print(update_order)
        return render(request, "tracker.html", {'order_items':order_items, 'update_order':update_order})
    return render(request, "tracker.html", {'cartItems':cartItems})

class Product_list(ListView):
    model = product
    template_name = 'things_list.html'
    
    def get_queryset(self):
        
        queryset = things.objects.all()
        if self.request.GET.keys():
           if self.request.GET.get('src') != '':
                keyword = self.request.GET.get('src')
                queryset = things.objects.filter(Q(title = keyword.capitalize()) | Q(title = keyword.capitalize()))
        return queryset