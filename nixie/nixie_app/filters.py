import django_filters
from .models import Product


class ProductFilter(django_filters.FilterSet):
    ordering = django_filters.OrderingFilter(fields=[('price', 'По цене'), ('name', 'По названию')], label="Сортировка")

    class Meta:
        model = Product
        fields = ['material', 'lamp_currency', 'lamp_type']
