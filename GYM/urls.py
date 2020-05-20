from django.contrib import admin
from django.urls import path,include
from GYM import views
from django.views.generic.base import RedirectView

urlpatterns = [    
path('enroll/<int:schedule_id>/',views.enroll, name='enroll'),
    
path('GYM/',RedirectView.as_view(url='index/')),
path('index/<int:id>/', views.index,name='index'), 
path('admin_login/',views.admin_login,name='admin_login'),
path('gymadmin/<int:id>',views.gymadmin,name='gymadmin'),
path('insert/',views.insert,name='insert'),
path('schedule/<int:id>',views.schedule,name='schedule'),
path('update/<int:id>',views.update,name='update'),
path('delete/<int:id>',views.delete,name='delete'),
path('trainer/<int:id>',views.trainer,name='trainer'),
path('Trainer_insert/',views.Trainer_insert,name='Trainer_insert'),
path('trainer_delete/<int:id>',views.trainer_delete,name='trainer_delete'),
path('trainer_update/<int:id>',views.trainer_update,name='trainer_update'),



path('registration/<int:id>',views.registration, name='registration'),


]
