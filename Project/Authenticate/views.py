from email import message
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import *
from django.core.mail import send_mail
from django.conf import settings
## iphcdpehtpukzkml
# Create your views here.
def home(request):
    return render(request, 'home.html')

def register(request):
    user = UserForm()
    registered = False
     
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        
        
        if user_form.is_valid():
            
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            
            username = request.POST.get('username')
            email = request.POST.get('email')
            
            subject = "Registered Successfully !"
            message = f"Hello {username} Thanks for registering, you can now log in to access our products. We sure will deliver. Aqua-Daive(sweetness in every drop)"     
            from_mail = settings.EMAIL_HOST_USER
            to = [email]
            
            send_mail(
                subject,
                message,
                from_mail,
                to,
                fail_silently=False,
            )
            registered = True
            return redirect('success')
    else:
        user_form=UserForm()
    
    
        
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
    return render(request, 'success.html')