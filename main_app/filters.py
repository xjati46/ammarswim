from admin_app.models import Order
import django_filters
from django import forms
from django.db import models


class OrderFilter(django_filters.FilterSet):
    student__nama_lengkap = django_filters.CharFilter(field_name='student__nama_lengkap', lookup_expr='icontains')

    class Meta:
        model = Order
        fields = ['student__nama_lengkap', 'coach', 'product', 'arsip']
        filter_overrides = {
            models.BooleanField: {
                'filter_class': django_filters.BooleanFilter,
                'extra': lambda f: {
                    'widget': forms.CheckboxInput,
                },
            },
        }
