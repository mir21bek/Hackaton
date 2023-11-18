from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryProductAdminViewSet, CategoryProduct

router = DefaultRouter()
router.register(r'category-admin', CategoryProductAdminViewSet)

urlpatterns = [
    path("category/<slug:category_slug>/", CategoryProduct.as_view())
    
]+router.urls