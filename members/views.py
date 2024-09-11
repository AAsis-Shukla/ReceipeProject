from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from members.models import Member
# Create your views here.
def first(request):
    return HttpResponse(loader.get_template('myfirst.html').render())
   
def my_members(request):
    temp = loader.get_template('all_members.html')
    member = Member.objects.all()
    myDict = {
        'members': member
    }
    return HttpResponse(temp.render(myDict,request))