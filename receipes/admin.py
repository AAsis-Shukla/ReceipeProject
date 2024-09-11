from django.contrib import admin
from receipes.models import *
# Register your models here.
class dfs(admin.ModelAdmin):
    list_display=['Receipe_name','Receipe_description','Receipe_image','user']
admin.site.register(Receipe,dfs)