from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth.models import User


def login(request):
    context = {}
    if request.POST:
        username = request.POST.get("username", '')
        password = request.POST.get("password", '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/catalog/packs/")
        else:
            context['login_error'] = "incorrect authorization data"
            return render(request, "auth_page.html", context)
    else:
        return render(request, "auth_page.html")


def logout(request):
    auth.logout(request)
    return redirect("/")
