from django.contrib.auth import authenticate, login
from django.db.models import deletion
from django.shortcuts import redirect, render
from django.http import JsonResponse
from . models import *
import json
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def home (request):
    products= Product.objects.all()
    category = Category.objects.all()
    context= {'products': products, 'category':category}
    return render (request, 'index.html', context)



def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_item':0}
    context = {'items': items, 'order': order}
    
    return render(request, 'cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'checkout.html', context)


def contact(request):
    context = {}
    return render(request, 'contact.html', context)


def about(request):
    context = {}
    return render(request, 'about.html', context)


def wishlist(request):
    context = {}
    return render(request, 'wishlist.html', context)


def shop(request):
    category = request.GET.get('category')
    if category == None:
        products = Product.objects.all()
    else:
        products = Product.objects.filter(category__name= category)



    products = Product.objects.all()

    categories = Category.objects.all()
    context = {'products': products, 'categories': categories}
    return render(request, 'shop-left-sidebar.html', context)


def product(request, myid):
    product = Product.objects.filter(id = myid)
    return render(request, 'single-product.html', {'product':product})


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action:', action)
    print('ProductId:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    elif action == 'delete':
        orderItem.quantity = 0
    

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete() 


    return JsonResponse('Item was added', safe=False)



def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username)
            login(request, user)
            messages.success(request, ("Registration Successful!"))
            return redirect( 'home' )
    else: 
        form = UserCreationForm()

    
    return render(request, 'register.html', {'form': form} )