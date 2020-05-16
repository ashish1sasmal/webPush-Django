from django.shortcuts import render,redirect
from django.contrib import messages
from django.http.response import JsonResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
from django.contrib.auth import authenticate,login,logout

def user_login(request):
    if request.method=="POST":
        username=request.POST.get('user')
        password=request.POST.get('pass')
        user=authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                print("success")
                messages.success(request,"Successfully logged in !")
                return redirect('/?status=1')
            else:
                pass
        else:
            messages.warning(request,"Wrong username or password!")
    return render(request,"login.html")

def home(request):
    return render(request,'home.html')
