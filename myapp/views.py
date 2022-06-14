from django.http import Http404
from django.shortcuts import get_list_or_404, redirect, render
from .models import *
from django.contrib.auth.models import User, auth
from datetime import datetime

def home_view(request, *args, ** kwargs):
    arts = Art.objects.all()
    tags = Tag.objects.values('tag').distinct()
    context = {
        'arts': arts,
        'tags': tags
    }
    return render(request, "index.html", context)

def cat(request, id, *args, **kwargs):
    arts=Tag.objects.filter(tag=id)
    return render(request, 'category.html', {'arts':arts})
    
def description_view(request, id, *args, **kwargs):
    art = Art.objects.get(id=id)
    context = {
        'art': art
    }
    return render(request, 'description.html', context)


def add(request, id, *args, **kwargs):
    # print(request.path())
    if (not request.user.is_authenticated):
        return redirect('../../../login/login')
    user_obj = User.objects.filter(username=request.user)
    art_obj = Art.objects.filter(id=id)
    check = MyCart.objects.filter(user=request.user,art_id=id)
    if len(check) != 0:
        print("Art Exits!!")
    else:
        obj = MyCart.objects.create(
            user=user_obj[0], art_id=art_obj[0], added_date=datetime.now())
        obj.save()
    return redirect('../../../')

    
def remove(request, id,*args, **kwargs):
    cart_obj = MyCart.objects.get(art_id= id)
    cart_obj.delete()
    
    return redirect('cart')


def about_us_view(request, *args, **kwargs):
    # about us
    return render(request, "aboutus.html", {})


def cart_view(request, *args, **kwargs):
    user_obj = User.objects.get(username=request.user)
    cart_obj = MyCart.objects.filter(user=user_obj)
    img = list()
    for item in cart_obj:
        artObj = Art.objects.get(id=item.art_id.id)
        img.append(artObj)

    con = zip(cart_obj, img)
    context = {
        'con': con
    }

    return render(request, "cart.html", context)


def order(request,id, *args, **kwargs):
    user_obj = User.objects.get(username=request.user)
    print(id)
    art_obj = Art.objects.get(id = id)
    obj = MyOrder.objects.create(user = user_obj, art_id = art_obj)
    obj.save()
    cart_obj = MyCart.objects.filter(art_id = art_obj)
    cart_obj.delete()
    art_obj.instock = False
    art_obj.save()
    return redirect('cart')

def order_view(request, *args, **kwargs):
    user_obj = User.objects.get(username=request.user)
    order_obj = MyOrder.objects.filter(user=user_obj)
    img = list()
    for item in order_obj:
        artObj = Art.objects.get(id=item.art_id.id)
        img.append(artObj)

    con = zip(order_obj, img)
    context = {
        'con': con
    }
    return render(request,"order.html",context)



