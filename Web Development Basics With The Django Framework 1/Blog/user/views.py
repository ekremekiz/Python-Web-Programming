from django.shortcuts import render
from user import forms
# Create your views here.

def register(request):
    form = forms.RegisterForm()
    context = {
        "form": form
    }
    return render(request, "register.html", context)

def loginUser(request):
    return render(request, "login.html")

def logoutUser(request):
    pass