from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, Http404
from django.contrib import auth
from django.contrib.auth.models import User
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from .models import *


def login(request):
    if request.user.is_authenticated:
        return redirect('catalog:packs')

    context = {}
    if request.POST:
        username = request.POST.get("username", '')
        password = request.POST.get("password", '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            try:
                user.userprofile
            except:
                userprofile = UserProfile.objects.create(user=user)
            return redirect("/catalog/packs/")
        else:
            context['login_error'] = "incorrect authorization data"
            return render(request, "auth_page.html", context)
    else:
        return render(request, "auth_page.html")


def logout(request):
    auth.logout(request)
    return redirect("/")


def signup(request):
    return Http404("Coming soon")


class RegisterFormView(FormView):
    form_class = UserCreationForm

    # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
    # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
    success_url = '/auth/login/'

    # Шаблон, который будет использоваться при отображении представления.
    template_name = "sign_up.html"

    def form_valid(self, form):
        # Создаём пользователя, если данные в форму были введены корректно.
        form.save()

        # Вызываем метод базового класса
        return super(RegisterFormView, self).form_valid(form)
