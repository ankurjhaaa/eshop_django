from django.contrib import admin
from django.urls import path,include
from eshopapp.views import (
    homepage,
    loginpage,
    signuppage,
    logoutpage,
    productview,
    cartpage,
    shoppage, 
    wishlistfunction,
    cartFunction,
    test_api
)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", homepage, name="home"),
    path("login/", loginpage, name="login"),
    path("signup/", signuppage, name="signup"),
    path("logout/", logoutpage, name="logout"),
    path("view/<slug:slug>/", productview, name="productview"),
    path("cart/", cartpage, name="cart"),
    path("shop/", shoppage, name="shop"),
    path("wishlistfunction/",wishlistfunction,name="wishlistfunction"),
    path("cartFunction/",cartFunction,name="cartFunction"),
    path('api/test/',test_api),
    path("api/", include("eshopapp.urls"))
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
