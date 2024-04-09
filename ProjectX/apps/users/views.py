from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from .models import User
from .forms import *
from django.views.generic import View, FormView

from django.views.generic import (
    View,
)
from django.views.generic.edit import (
    FormView,
    UpdateView
)
from .forms import LoginForm


class LoginUser(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('biblioteca_app:list-libros')

    def form_valid(self, form):
        user = authenticate(
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password']
        )
        login(self.request, user)
        return super(LoginUser, self).form_valid(form)


class LogoutUser(View):
    def get(elf, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(
            reverse(
                'users_app:user-login'
            )
        )


class CreateUser(FormView):
    template_name = 'register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('users_app:user-login')

    def form_valid(self, form):
        usuario = User.objects.create_user(
            form.cleaned_data['email'],
            form.cleaned_data['password'],
            nombre=form.cleaned_data['nombre'],
            apellido=form.cleaned_data['apellido'],
            usertype='VIEW',
            is_active=True,
        )
        return super().form_valid(form)
