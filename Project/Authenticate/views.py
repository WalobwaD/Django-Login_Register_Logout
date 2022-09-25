from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import *

# Create your views here.
def home(request):
    return render(request, 'home.html')

def register(request):
    registered = False
     
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        
        if user_form.is_valid():
            
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            
            
            registered = True
    else:
        user_form = UserForm()
        
    context = {
        'user_form' : user_form,
        'registered' : registered,
    }
        
                    
    return render(request, 'registration.html', context)

def user_login(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user:
            if  user.is_active:
                login(request, user)
                return redirect('home')
            else:
                return HttpResponse('ACCOUNT IS NOT ACTIVE!')
        else:
            return HttpResponse('INVALID CREDENTIALS!')
    else:
        return render(request, 'login.html')


@login_required
def user_logout(request):
    logout(request)
    return redirect('home')

@login_required
def special(request):
    return HttpResponse('You have logged in successfully')