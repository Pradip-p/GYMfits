from django.contrib import admin
from django.urls import path,include
from GYM import views
from django.views.generic.base import RedirectView

urlpatterns = [    
path('GYM/',RedirectView.as_view(url='index/')),
#path('GYM/',views.index, name='index'),
path('index/<int:id>/', views.index,name='index'), 
path('signup/',views.signup, name='signup'),
path('login/',views.login, name='login'),
path('registration/',views.registration, name='registration'),
path('gymadmin/',views.gymadmin, name='gymadmin'),
path('activate/<uidb64>/<token>/',views.activate, name='activate'),

]
