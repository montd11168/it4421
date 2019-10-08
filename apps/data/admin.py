from django.contrib import admin

from .models import (
    Comment,
    Export,
    Import,
    Item,
    Order,
    Product,
    ProductColor,
    ProductImage,
    Supplier,
    Vote,
)


class CommentAdmin(admin.ModelAdmin):
    list_display = ("user", "product", "content", "time")
    readonly_fields = ("time",)
    search_fields = ("user", "product")


class ExportAdmin(admin.ModelAdmin):
    list_display = ("product", "quantity")
    search_fields = ("product",)


class ImportAdmin(admin.ModelAdmin):
    list_display = ("product", "quantity")
    search_fields = ("product",)


class ItemAdmin(admin.ModelAdmin):
    list_display = ("user", "product")
    search_fields = ("user", "product")


class OrderAdmin(admin.ModelAdmin):
    list_display = ("user", "status", "created")
    readonly_fields = ("created",)
    search_fields = ("user", "status")


class ProductAdmin(admin.ModelAdmin):
    search_fields = ("supplier", "name")


class ProductColorAdmin(admin.ModelAdmin):
    list_display = ("product", "color")
    search_fields = ("product", "color")


class ProductImageAdmin(admin.ModelAdmin):
    list_display = ("product", "descript")
    search_fields = ("product", "descript")


class SupplierAdmin(admin.ModelAdmin):
    search_fields = ("name",)


class VoteAdmin(admin.ModelAdmin):
    list_display = ("user", "product", "value")
    search_fields = ("user", "product", "value")


admin.site.register(Comment, CommentAdmin)
admin.site.register(Export, ExportAdmin)
admin.site.register(Import, ImportAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductColor, ProductColorAdmin)
admin.site.register(ProductImage, ProductImageAdmin)
admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Vote, VoteAdmin)
