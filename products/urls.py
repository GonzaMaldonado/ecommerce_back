from django.urls import path, include
from .views import get_product, get_products, ProductViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'product', ProductViewSet, basename='product')

urlpatterns = [
    path('products/', get_products),
    path('get/<str:name>/', get_product),
    path('', include(router.urls)),
]