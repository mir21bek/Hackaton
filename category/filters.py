import django_filters
from .models import Category

class CategoryFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(name='title', lookup_expr='iexact')

    class Meta:
        model = Category
        fields = ['category']
