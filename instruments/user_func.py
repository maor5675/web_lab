from user.models import User
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm



def elogin(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'user does not exist')
            return redirect('lab:login')
        
        authuser = authenticate(request,username=username, password=password)
        if authuser:
            login(request, authuser)
            return redirect('lab:login')
        else:
            messages.error(request, 'Incorrect password')
            return redirect('lab:login')

    else:
        context = {}
        return render(request,'user/login.html',context=context)


def elogout(request):
    logout(request)
    return redirect('lab:mainlab')     


def eregister(request):
    if request.POST:
        user_form = UserForm(request.POST,request.FILES)
        if  user_form.is_valid():
            user_form.save()
            return redirect ("lab:mainlab")

    else:
        User = UserForm()
        context ={
            'form' : User,
            'name' : 'register' # i need the name for enter the correct erea in the html
        }
        return render(request,'user/login.html',context=context)
        