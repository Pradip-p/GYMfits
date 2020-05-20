from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from . models import GymInfromation,UserInformation
from GYM.models import Trainers, Schedule
# Register your models here.
admin.site.register(UserInformation)
admin.site.register(Schedule)




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




