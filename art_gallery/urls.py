"""art_gallery URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from myapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name = 'home'),
    path('aboutus/', about_us_view, name = 'about'),
    path('cart/', cart_view, name = 'cart'),
    path('order/', order_view, name = 'order'),
    path('login/',include('login.urls')),
    path('description/<int:id>/', description_view, name = 'description'),
    path('description/<int:id>/add/', add, name = 'add'),
    path('cart/order/<int:id>', order, name = 'order'),
    path('cart/remove/<int:id>', remove, name = 'remove'),
    path('staffaccount/',include('staff_account.urls')),    
    path('cat/<str:id>', cat, name = 'cat'),
 ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
