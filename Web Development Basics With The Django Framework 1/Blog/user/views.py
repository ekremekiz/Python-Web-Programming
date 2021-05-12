from django.shortcuts import render, redirect
from user import forms
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
# Create your views here.

def register(request):
    form = forms.RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        newUser = User(username=username)
        newUser.set_password(password)

        newUser.save()
        login(request, newUser)
        messages.info(request, "Başarıyla Kaydoldunuz")
        return redirect("index")
    context = {
        "form": form
    }
    return render(request, "register.html", context)

    """
    if request.method == "POST":
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            newUser = User(username = username)
            newUser.set_password(password)

            newUser.save()
            login(request, newUser)
            return redirect("index")
        context = {
            "form": form
        }
        return render(request, "register.html", context)

    else:
        form = forms.RegisterForm()
        context = {
            "form":form
        }
        return render(request, "register.html", context)
    """
def loginUser(request):
    form = forms.LoginForm(request.POST or None)
    context = {
        "form": form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username=username, password=password)

        if user is None:
            messages.info(request, "KUllanıcı Adı veya Parola Hatalı")
            return render(request, "login.html", context)

        messages.success(request, "Başarıyla Giriş Yapıldı")
        login(request, user)
        return redirect("index")
    return render(request, "login.html", context)


    return render(request, "login.html")

def logoutUser(request):
    logout(request)
    messages.success(request, "Başarıyla Çıkış Yapıldı")
    return redirect("index")
