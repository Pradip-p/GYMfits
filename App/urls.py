from django.contrib import admin
from django.urls import path,include
from . import views
from django.views.generic.base import RedirectView



urlpatterns = [    
#path('',RedirectView.as_view(url='index/')),
path('',views.index, name='index'),
path('index/', views.index,name='index'), 
path('contact/', views.contact, name='contact'),
path('logout/',views.logout, name='logout'),
path('login/',views.login, name='login'),
path('signup/',views.signup, name='signup'),  
path('activate/<uidb64>/<token>/',views.activate, name='activate'),

]
