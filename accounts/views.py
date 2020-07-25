from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages

# Create your views here.


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 != password2:
            messages.info(request, 'Password did not match')
            return redirect('signup')
        elif User.objects.filter(username=username).exists():
            messages.info(request, 'User name already exists')
            return redirect('signup')
        else:
            users = User.objects.create_user(username=username, password=password1)
            users.save();

        return redirect('home')

    else:
        return render(request, 'accounts/signup.html')



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password not correct')
            return redirect('login')

    else:
        return render(request, 'accounts/login.html')


def logout(request):
    auth.logout(request)
    return redirect('home')
    # if request.method == 'POST':

