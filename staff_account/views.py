from django.shortcuts import render, redirect
from django.contrib import auth
from django.http import request
from myapp.models import *

# Create your views here.


def stafflogin(request, *args, ** kwargs):

    return render(request, 'stafflogin.html', {})


def checkStaff(request, *args, **kwargs):
    if request.method == 'POST':
        user_name = request.POST.get('user_name', False)
        password = request.POST['password']
        user = auth.authenticate(
            username=user_name, password=password, staff=True)
        if user is not None:
            print(request.user)
            auth.login(request, user)
            return render(request, 'artoperations.html', {})
    return redirect('stafflogin')


def add_art(request, *args, **kwargs):
    art = Art.objects.all()
    artist = Artist.objects.all()
    print("\n art \n")
    context = {
        'art': art,
        'artist': artist,
    }
    return render(request, "artoperations.html", context)


def upload(request, *args, **kwargs):
    if request.method == 'POST':
        art_name = request.POST['art_name']
        artist_name = request.POST['artist_name']
        artist = Artist.objects.get(id = artist_name.split()[0])
        description = request.POST['description']
        price = request.POST['price']
        image = request.POST['image']
        newart = Art.objects.create(art_name=art_name,
                                    price=price,
                                    art_artist=artist,
                                    image=image,
                                    description = description
                                    )
        print(art_name, artist_name, description, price)
        newart.save()
        art = Art.objects.all()
    else:
        return redirect('home')

    context = {
        'art': art,
    }
    return render(request, "artoperations.html", context)
