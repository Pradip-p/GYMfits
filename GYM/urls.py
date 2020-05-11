from django.contrib import admin
from django.urls import path,include
from GYM import views
from django.views.generic.base import RedirectView

urlpatterns = [    
path('GYM/',RedirectView.as_view(url='index/')),
#path('GYM/',views.index, name='index'),
path('index/<int:id>/', views.index,name='index'), 
path('gymadmin/',views.gymadmin,name='gymadmin'),
path('insert/',views.insert,name='insert'),
path('schedule/',views.schedule,name='schedule'),
path('update/<int:id>',views.update,name='update'),
path('delete/<int:id>',views.delete,name='delete'),
path('registration/',views.registration, name='registration'),


]
