from django.shortcuts import render, redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User


def register(request):
    if request.method == "POST":
        context = {
            "values": request.POST
        }
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['Confirm password']
        
        if password == password2:
            #check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken')
                return render(request, "accounts/register.html", context)
        
            #check user email
            if User.objects.filter(email=email).exists():
                messages.error(request, 'That email is taken')
                return render(request, "accounts/register.html", context)
            

            user = User.objects.create_user(
                username=username,
                password=password,
                first_name= first_name,
                last_name=last_name
            )
            user.save()
            messages.success(request, 'You are now registered')
            return redirect('login')
        
        else:
            messages.error(request, 'Passwords do no match!')
            return render(request, "accounts/register.html", context)
        
def login(request):
    if request.method == "POST":
        context = {
            "values": request.POST
        }
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        messages.error(request, 'Invalid credentials')
        return render(request, 'accounts/login.html', context)
    
def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, 'You are noe logged out')
        return redirect('index')
    return render(request, "accounts/login.html")