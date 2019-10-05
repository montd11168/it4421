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
    list_display = ("user", "product")
    readonly_fields = ('time',)


class ExportAdmin(admin.ModelAdmin):
    pass


class ImportAdmin(admin.ModelAdmin):
    pass


class ItemAdmin(admin.ModelAdmin):
    list_display = ("user", "product")


class OrderAdmin(admin.ModelAdmin):
    list_display = ("user", "status")
    readonly_fields = ('created',)


class ProductAdmin(admin.ModelAdmin):
    pass


class ProductColorAdmin(admin.ModelAdmin):
    list_display = ("product", "color")


class ProductImageAdmin(admin.ModelAdmin):
    list_display = ("product", "descript")


class SupplierImageAdmin(admin.ModelAdmin):
    pass


class VoteImageAdmin(admin.ModelAdmin):
    list_display = ("user", "product")


admin.site.register(Comment, CommentAdmin)
admin.site.register(Export, ExportAdmin)
admin.site.register(Import, ImportAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductColor, ProductColorAdmin)
admin.site.register(ProductImage, ProductImageAdmin)
admin.site.register(Supplier, SupplierImageAdmin)
admin.site.register(Vote, VoteImageAdmin)
