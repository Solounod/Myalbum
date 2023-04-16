from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django import forms
from .form import UserCreationFormStyle, AuthenticationFormStyle
# Create your views here.

class MyViewPage(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'createuser/index.html')

class MyView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'createuser/index.html')

class RegisterUser(View):
    
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('logout')
        else:
            form = UserCreationFormStyle()
            if request.method == "GET":
                return render(request, 'registration/registration.html', {"form":form})
        
    def post(self, request):
        form = UserCreationFormStyle(request.POST)
        if form.is_valid():
            usercreated = form.save()
            #login(request, usercreated)
            return redirect('login')
        
        
        return render(request, 'registration/registration.html', {"form":form})
    
    def logout_user(request):
        logout(request)
        return redirect('home')


class LoginUser(View):
    
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('logout')
        else:
            if request.method == "GET":
                return render(request, 'registration/login.html', {"form":AuthenticationFormStyle})

    def post(self, request):
        if request.method == "POST":
            form = AuthenticationFormStyle(request, data = request.POST)
            if form.is_valid():
                name_user = form.cleaned_data.get("username")
                user_pass = form.cleaned_data.get("password")
                user_auth = authenticate(username=name_user, password=user_pass)
                if user_auth is not None:
                    login(request, user_auth)
                    return redirect('home')
                else:
                    messages.error(request, "EL usuario o la contraceña no son validos")  
            else:
                messages.error(request, "EL usuario o la contraceña no son validos")

        
        form = AuthenticationFormStyle()
        return render(request, 'registration/login.html', {"form":form})