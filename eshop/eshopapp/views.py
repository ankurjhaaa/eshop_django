from django.shortcuts import render, redirect, HttpResponse
from .models import Category, Product, Wishlist
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def homepage(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    wishlist = []
    
    if request.user.is_authenticated:
        wishlist = Wishlist.objects.filter(user_id = request.user).values_list('product_id_id',flat=True)
        
    return render(
        request,
        "public/home.html",
        {"categories": categories, "products": products,"wishlist" : wishlist},
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


def cartpage(request):
    return render(request, "public/cart.html")


def productview(request, slug):
    product = Product.objects.filter(slug=slug).first()
    user_id = request.user
    isWishlist = Wishlist.objects.filter(user_id=user_id, product_id=product).first()
    return render(
        request,
        "public/productview.html",
        {"product": product, "isWishlist": isWishlist},
    )


def shoppage(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    categoryFilter = request.GET.get("category")
    searchFilter = request.GET.get("search")
    if categoryFilter:
        catId = Category.objects.filter(slug=categoryFilter).first()
        products = Product.objects.filter(cat_id=catId)
    if searchFilter:
        products = Product.objects.filter(name__icontains=searchFilter)

    countTotal = products.count()
    return render(
        request,
        "public/shop.html",
        {"products": products, "categories": categories, "countTotal": countTotal},
    )


def wishlistfunction(request):
    product_id = request.GET.get("product_id")
    product = Product.objects.filter(id=product_id).first()
    user_id = request.user
    checkLiked = Wishlist.objects.filter(user_id=user_id, product_id=product_id).first()
    if checkLiked:
        checkLiked.delete()
    else:
        Wishlist.objects.create(user_id=user_id, product_id=product)

    return redirect(request.META.get("HTTP_REFERER", "home"))
