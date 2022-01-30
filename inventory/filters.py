import django_filters
from .models import Stock


class StockFilter(django_filters.FilterSet):                            # Stockfilter used to filter based on name
    hersteller = django_filters.CharFilter(lookup_expr='icontains')           # allows filtering without entering the full name
    grundmaterial = django_filters.CharFilter(lookup_expr='icontains')           # allows filtering without entering the full name
    artikel = django_filters.CharFilter(lookup_expr='icontains')           # allows filtering without entering the full name
    artikelnummer = django_filters.CharFilter(lookup_expr='icontains')           # allows filtering without entering the full name

    class Meta:
        model = Stock
        fields = ['hersteller', 'grundmaterial', 'artikel', 'artikelnummer']
