from tkinter.messagebox import NO
from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.views import View
from django import forms
from django.db.models import Q
# Create your views here.

def base(request):
    return render (request,'base.html')

def index(request):
    mobile_product = Product.objects.filter(catagory="M")
    context = {'mobile_product':mobile_product}
    laptop_product = Product.objects.filter(catagory="L")
    context["laptop_product"] = laptop_product
    return render (request,'index.html',context)

def registration_page(request):
    fm = MyUserCreationForm(request.POST or None)
    context = {'fm':fm}
    if fm.is_valid():
        fm.save()
        messages.success(request,"Registration Done , Login Now !!")
    return render (request,'registration_page.html',context)

def profile(request,id):
    obj = User.objects.get(id=id)
    print(obj.username)
    fm=CustomerForm(request.POST or None)
    context={'fm':fm}
    if fm.is_valid():
        name = fm.cleaned_data['name']
        locality = fm.cleaned_data['locality']
        city = fm.cleaned_data['city']
        pincode = fm.cleaned_data['pincode']
        mobile_number = fm.cleaned_data['mobile_number']
        customer = Customer(user=obj,name=name,locality=locality,city=city,pincode=pincode,mobile_number=mobile_number)
        customer.save()
        messages.success(request,"Your Profile Has been Updated !!")
    return render (request,'registration/profile.html',context)

def add_profile(request,id):
    obj = User.objects.get(id=id)
    fm=CustomerForm(request.POST or None)
    context={'fm':fm}
    if fm.is_valid():
        name = fm.cleaned_data['name']
        locality = fm.cleaned_data['locality']
        city = fm.cleaned_data['city']
        pincode = fm.cleaned_data['pincode']
        mobile_number = fm.cleaned_data['mobile_number']
        customer = Customer(user=obj,name=name,locality=locality,city=city,pincode=pincode,mobile_number=mobile_number)
        customer.save()
        messages.success(request,"Your Profile Has been Added !!")
    return render (request,'registration/add_profile.html',context)

def edit_profile(request,id):
    obj = User.objects.get(id=id)
    customer = Customer.objects.get(user=obj)
    fm=CustomerForm(request.POST or None,instance=customer)
    context={'fm':fm}
    if fm.is_valid():
        fm.save()
        messages.success(request,"Your Profile Has been Updated !!")
        return render (request,'registration/edit_profile.html',context)

    return render (request,'registration/edit_profile.html',context)

def conatct(request):
    return render (request,'conatct.html')

def about(request):
    return render (request,'about.html')

def mobiles(request):
    product = Product.objects.filter(catagory="M")
    context = {'product':product}
    number = int(len(product))
    context['number'] = number
    return render (request,'product/mobiles.html',context)

def laptop(request):
    product = Product.objects.filter(catagory="L")
    context = {'product':product}
    number = int(len(product))
    context['number'] = number
    return render (request,'product/laptop.html',context)

def order(request,id):
    if request.user.is_authenticated:
        product = Product.objects.get(id=id)
        context = {'product':product}
        cart_item = False
        cart_item = Cart.objects.filter(Q(product=product.id) & Q(user=request.user)).exists()
        context["cart_item"] = cart_item
        return render (request,'order.html',context)
    else:
        return redirect ('/accounts/login')
def cart(request,id):
    product = Product.objects.get(id=id)
    context = {'product':product}
    user = request.user
    quantity = request.GET.get('quantity')
    cart = Cart(user=user,product=product,quantity=quantity)
    cart.save()
    return redirect ('kart')
def kart(request):
    user = request.user
    cart = Cart.objects.filter(user=user)
    context = {'cart':cart}
    amount = 0.0
    cart_product = [ p for p in Cart.objects.all() if p.user == user]
    if cart_product:
        pa = []
        for p in cart_product:
            tempamount = (p.quantity * p.product.discount_price)
            qq = p.quantity
            pp = p.product.discount_price
            t = qq * pp
            pa.append(t)
            context["pa"] = pa
            amount +=tempamount
            context["amount"] = amount
        return render (request,'kart.html',context)
    else:
        return render (request,'empty_kart.html')

def checkout(request):
    user = request.user
    customer = Customer.objects.filter(user=user)
    context = {'customer':customer}
    cart = Cart.objects.filter(user=user)
    context["cart"] = cart
    amount = 0
    cart_product = [ p for p in Cart.objects.all() if p.user == user]
    if cart_product:
        pa = []
        for p in cart_product:
            tempamount = (p.quantity * p.product.discount_price)
            qq = p.quantity
            pp = p.product.discount_price
            t = qq * pp
            pa.append(t)
            context["pa"] = pa
            amount +=tempamount
            context["amount"] = amount
        return render (request,'checkout.html',context)
    else:
        return render (request,'empty_kart.html')

def payment_page(request):
    user = request.user
    customer = Customer.objects.get(user=user)
    payment_method = request.GET.get('payment')
    context = {'customer':customer}
    cart = Cart.objects.filter(user=user)
    context["cart"] = cart
    for c in cart:
        OrderPlaced(user=user,customer=customer,product=c.product,quantity=c.quantity,payment_method=payment_method).save()
        c.delete()
    return redirect ('order_page')
    # OrderPlaced.objects.filter(user=user,customer=customer,product=c.product,quantity=c.quantity)
    

def order_page(request):
    user = request.user
    customer = Customer.objects.filter(user=user)
    context = {'customer':customer}
    oreder = OrderPlaced.objects.filter(user=user)
    if oreder:
        context["oreder"] = oreder
        return render (request,'order_page.html',context)
    else:
        return render (request,'empty_order_page.html')
def remove_item(request,id):
    user = request.user
    cart = Cart.objects.filter(id=id)
    cart.delete()
    return redirect ('kart')


def demo(request):
    return render (request,'demo.html')
