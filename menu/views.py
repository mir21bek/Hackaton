from rest_framework import generics, permissions, viewsets
from rest_framework.generics import get_object_or_404

from .models import Category, Menu
from .serializers import CategorySerializer, MenuSerializer


class CategoryApiView(generics.ListAPIView):
    """Представление для получения списка всех категорий.

    Это представление позволяет только чтение (GET) и требует аутентификации пользователя.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]


class CategoryCreateApiView(viewsets.ModelViewSet):
    """Представление для создания, обновления, удаления и получения категорий.

    Это представление позволяет создавать (POST), обновлять (PUT, PATCH), удалять (DELETE) и
    получать (GET) объекты категорий. Требует прав администратора для выполнения операций изменения.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]

    def perform_create(self, serializer):
        """Метод для создания новой категории и вызова сигнала после успешного создания."""
        category_instance = serializer.save()
        post_category_save(sender=Category, instance=category_instance, created=True)


class MenuListApiView(generics.ListAPIView):
    """Представление для получения списка доступных блюд.

    Это представление позволяет только чтение (GET) и требует аутентификации пользователя.
    """
    queryset = Menu.objects.all().filter(available=True)
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Menu.objects.filter(available=True)
        category_slug = self.kwargs.get('category_slug')
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            queryset = queryset.filter(category=category)
            return queryset


class PopularDishesView(generics.ListAPIView):
    serializer_class = MenuSerializer

    def get_queryset(self):
        return Menu.objects.filter(popular=True)[:5]


class MenuCreateUpdateApiView(viewsets.ModelViewSet):
    """Представление для создания, обновления, удаления и получения блюд.

    Это представление позволяет создавать (POST), обновлять (PUT, PATCH), удалять (DELETE) и
    получать (GET) объекты блюд. Требует прав администратора для выполнения операций изменения.
    """
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAdminUser]
