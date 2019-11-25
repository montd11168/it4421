from django.contrib import admin

from .models import (
    Comment,
    Export,
    Import,
    Cart,
    Order,
    Product,
    ProductImage,
    Supplier,
    Vote,
)


class CommentAdmin(admin.ModelAdmin):
    list_display = ("user", "product", "content", "created_at")
    readonly_fields = ("created_at",)
    search_fields = ("user", "product")


class ExportAdmin(admin.ModelAdmin):
    list_display = ("product", "quantity")
    search_fields = ("product",)


class ImportAdmin(admin.ModelAdmin):
    list_display = ("product", "quantity")
    search_fields = ("product",)


class CartAdmin(admin.ModelAdmin):
    list_display = ("user", "product")
    search_fields = ("user", "product")


class OrderAdmin(admin.ModelAdmin):
    list_display = ("user", "status", "created_at")
    readonly_fields = ("created_at",)
    search_fields = ("user", "status")


class ProductAdmin(admin.ModelAdmin):
    search_fields = ("supplier", "name")


class ProductImageAdmin(admin.ModelAdmin):
    list_display = ("product", "description")
    search_fields = ("product", "description")


class SupplierAdmin(admin.ModelAdmin):
    search_fields = ("name",)


class VoteAdmin(admin.ModelAdmin):
    list_display = ("user", "product", "value")
    search_fields = ("user", "product", "value")


admin.site.register(Comment, CommentAdmin)
admin.site.register(Export, ExportAdmin)
admin.site.register(Import, ImportAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage, ProductImageAdmin)
admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Vote, VoteAdmin)
