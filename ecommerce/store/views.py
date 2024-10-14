from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *
# Create your views here.
def store(request):
    products = Product.objects.all()
    context = {'products': products}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in")
            # Ensure the user has a Customer profile
            if not hasattr(user, 'customer'):
                Customer.objects.create(user=user)
            return redirect('store')
        else:
            messages.success(request, "There Was An Error Logging In, Please Try Again...")
            return redirect('store')
    else:
        return render(request, 'store/store.html', context)

def logout_user(request):
    logout(request)
    messages.success(request, "You Have Been Logged Out...")
    return redirect('store')

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        order = {'get_cart_total' : 0, 'get_cart_items' : 0}
        items = []
    context = {'items': items, 'order': order}
    return render(request, 'store/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)

 
