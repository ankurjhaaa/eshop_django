from django.shortcuts import render, redirect
from .models import Category, Product
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def homepage(request):
    return render(
        request,
        "public/home.html",
        {"categories": Category.objects.all(), "products": Product.objects.all()},
    )


def loginpage(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")

    return render(request, "auth/login.html")


def signuppage(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        User.objects.create_user(
            username=email, first_name=name, email=email, password=password
        )
        return redirect("login")

    return render(request, "auth/signup.html")


def logoutpage(request):
    logout(request)
    return redirect("home")


def productview(request, slug):
    return render(
        request,
        "public/productview.html",
        {"product": Product.objects.filter(slug=slug).first},
    )
