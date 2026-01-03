from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet,CategoryViewSet

router=DefaultRouter()
router.register(r"products",ProductViewSet,basename="productView")
router.register(r"categories",CategoryViewSet,basename="categoryView")
urlpatterns = [
    
    path("products",include(router.urls)),
    path("categories",include(router.urls)),
    
    
]
