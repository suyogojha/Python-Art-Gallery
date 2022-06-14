from django.urls import path
from . import views
from staff_account.views import add_art
urlpatterns = [
    path('',views.stafflogin, name="stafflogin"),
    path('checkStaff/',views.checkStaff, name="checkStaff"),
    path('artoperations', views.add_art, name = 'artoperations'),
    path('upload',views.upload,name='upload'),
]


