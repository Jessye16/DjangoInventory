from django.contrib import admin
from inventory.models import Product, Member
#Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'brand',
        'type',
        'gender',
        'description',
        'stock',
        'quantity',
        'created_by',
        'created_at',
        'modified_by',
        'modified_at'
    )

class MemberAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Member)