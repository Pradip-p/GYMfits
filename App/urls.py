from django.contrib import admin
from django.urls import path,include
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [    
#path('',RedirectView.as_view(url='index/')),
path('',views.index, name='index'),
path('index/', views.index,name='index'), 
path('contact/', views.contact, name='contact'),
#path('login/',views.login, name='login'),
path('logout/',views.logout, name='logout'),
#path('home/',views.home, name='home'),
#path('index/',views.HomeView.as_view()),
#path('about/',views.AboutView.as_view()),
#path('contact/',views.ContactView.as_view()),    
]
