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
