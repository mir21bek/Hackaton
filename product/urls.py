from django.urls import path
from rest_framework import routers

from .views import ProductAdminViewSet,ProductListAPIView


router = routers.DefaultRouter()
router.register(r'product-crud',ProductAdminViewSet,basename='product-crud')


urlpatterns = [

    path('products/', ProductListAPIView.as_view())

]+router.urls



