from django.shortcuts import render, redirect
from django.db.models.functions import Lower
from django.core.mail import send_mail
from receipes.models import Receipe
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login, logout
from django.contrib.auth.decorators import login_required 
from .forms import *
import os
# Create your views here.
@login_required(login_url='receipe_login')
def Receipes(request):
    if request.method == "GET":
        filter_by = request.GET.get('filter_by', None)
        filter_input = request.GET.get('filter_input', None)
        sort_by = request.GET.get('sort_by', None)

        if filter_by and filter_input: 
            if filter_by == 'name':
                form = Receipe.objects.filter(Receipe_name__icontains=filter_input)
            elif filter_by == 'id':
                form = Receipe.objects.filter(id__icontains=filter_input)
            elif filter_by == 'desc':
                form = Receipe.objects.filter(Receipe_description__icontains=filter_input)
            else:
                form = None
            return render(request, 'index.html', {'form': form,'form_length':len(form)})
        if sort_by == 'name':
            form = Receipe.objects.all().order_by(Lower('Receipe_name'))
            return render(request, 'index.html', {'form': form,'form_length':len(form)})
        if sort_by == 'latest':
            form = Receipe.objects.all().order_by('-id')
            return render(request, 'index.html', {'form': form,'form_length':len(form)})
        else:
            pass
    if request.method == "POST":
        data = request.POST
        Receipe_name  = request.POST['Receipe_name']
        Receipe_description = request.POST['Receipe_description']
        Receipe_image = request.FILES.get('Receipe_image')
        E_msg = f"Receipe Name = {Receipe_name}\n Receipe Description = {Receipe_description}\n Receipe image = {Receipe_image}"
        existence = Receipe.objects.filter(Receipe_name = Receipe_name,Receipe_description = Receipe_description).exists()
        if not existence:
            Receipe.objects.create(Receipe_name = Receipe_name,Receipe_description = Receipe_description,Receipe_image = Receipe_image,user=request.user)
            send_mail(
            "Submitted Response!",
            E_msg,
            "asiskumar734@gmail.com",
            [request.POST['E_response']],
            fail_silently=False,
            )
            return render(request,'index.html',{'seccess_msg':'Added Successfully!'})
        else:
            return render(request,'index.html',{'error_msg':'Already Added!'})

    return render(request,'index.html',{'form':Receipe.objects.filter(user__username = request.user.username),'form_length':len(Receipe.objects.filter(user__username = request.user.username))})
    
@login_required()
def deleteItem(request,id):
    previous = Receipe.objects.get(id=id)
    previous.Receipe_image.delete()
    previous.Receipe_image = None
    previous.delete()
    return redirect(Receipes)
@login_required()
def updateItem(request,id):
    previous = Receipe.objects.get(id=id)
    if request.method == "POST":
        previous.Receipe_name  = request.POST['Receipe_name']
        previous.Receipe_description = request.POST['Receipe_description']
        Receipe_image = request.FILES.get('Receipe_image')
        if Receipe_image:
            previous.Receipe_image.delete()
            previous.Receipe_image = Receipe_image
            previous.save()
        else:
            previous.save()
        return redirect(Receipes)
    return render(request,'update_receipe.html',{'form':previous})

def receipe_register(request):
    if request.method == 'POST':
        name = request.POST.get('Name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if User.objects.filter(username = email).exists():
            return render(request,'signUp.html',{'success_message':'Account is already exist!'})
        user = User.objects.create(first_name = name, username = email)
        user.set_password(password)
        user.save()
        return render(request,'signUp.html',{'success_message':'Account created successfully!'})
    return render(request,'signUp.html')
def receipe_login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        if not User.objects.filter(username = email):
            return render(request,'login.html',{'error_msg':'Invalid Username!'})
        user = authenticate(username = email , password =  password)
        if user is None:
            return render(request,'login.html',{'error_msg':'Invalid password!'})
        else:
            login(request, user) 
            return redirect(Receipes)
        
            
    return render(request,'login.html')

def receipe_logout(request):
    logout(request)
    return redirect(receipe_login)