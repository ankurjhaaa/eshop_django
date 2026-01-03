from rest_framework import serializers
from .models import Product,Category,Wishlist

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields="__all__"
        
class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields="__all__"
        
        