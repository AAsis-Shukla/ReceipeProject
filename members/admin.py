from django.contrib import admin
from members.models import *

# Register your models here.
class modelAdmin(admin.ModelAdmin):
    list_display = ('id','firstName','lastName','phone','joined_date')
admin.site.register(Member,modelAdmin)