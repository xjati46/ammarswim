from django.contrib import admin
from admin_app.models import Product, Order
from import_export.admin import ImportExportModelAdmin

# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'id')


@admin.register(Order)
class OrderAdmin(ImportExportModelAdmin):
    list_display = ('__str__', 'student', 'coach', 'arsip')
    list_filter = ('coach', 'arsip')
    fields = [
        ('student', 'coach'),
        ('product', 'jenis_order'),
        ('tanggal_transaksi', 'tanggal_expired'),
        'diskon',
        ('p1', 'p1_c'),
        ('p2', 'p2_c'),
        ('p3', 'p3_c'),
        ('p4', 'p4_c'),
        ('p5', 'p5_c'),
        ('p6', 'p6_c'),
        ('p7', 'p7_c'),
        ('p8', 'p8_c'),
        'arsip'
        ]
