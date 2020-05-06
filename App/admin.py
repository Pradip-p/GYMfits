from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from . models import GymInfromation
from GYM.models import Trainers,Registration
# Register your models here.





class RegistrationAdmin(ModelAdmin):
    list_display=['first_name','last_name','address','email','gender','phone_number','status','age','time']
    search_fields=['first_name','phone_number','age','gender','status']
    list_filter=['status','age','time']
admin.site.register(Registration,RegistrationAdmin)



class TrainerAdmin(ModelAdmin):
    list_display=['name','phone_number','age','trainer_type','address','about']
    list_filter=['name','age','trainer_type']
    search_fields=['name','trainer_type','address','age','phone_number']
admin.site.register(Trainers,TrainerAdmin)
admin.site.register(GymInfromation)




#class GymInfromationAdmin(ModelAdmin):
    #list_display=['name','owner_name','location','phone_number','pricing','rating_count','summary']
    #list_filter=['name','phone_number','location']
    #search_fields=['name','owner_name','phone_number','location','pricing']




