from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect


# from .models import

def user_login(request):
    if request.user.is_authenticated:
        return redirect("/")
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return redirect("/login/")
    else:
        pass
    return render(request, 'account/index.html')


def user_register(request):
    context = {"errors": []}
    if request.user.is_authenticated:
        return redirect("/")
    if request.method == "POST":
        username = request.POST.get("username").lower()
        username = request.POST.get("username").lower()
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        name = request.POST.get("name").capitalize()
        lastname = request.POST.get("lastname").capitalize()
        if password1 != password2:
            context['errors'].append('passwords do not match')
            return render(request, 'account/register.html', context)
        # if User.objects.get(username=username):
        #     context['errors'].append('this username is exist')
        #     return render(request, 'account/register.html', context)

        User.objects.create_user(username=username, password=password1, email=email, first_name=name, last_name=lastname)
        user = authenticate(request, username=username, password=password1)
        login(request, user)
    return render(request, 'account/register.html')


def user_logout(request):
    logout(request)
    return redirect('/')
