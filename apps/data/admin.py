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

admin.site.register(Comment)
admin.site.register(Export)
admin.site.register(Import)
admin.site.register(Item)
admin.site.register(Order)
admin.site.register(Product)
admin.site.register(ProductColor)
admin.site.register(ProductImage)
admin.site.register(Supplier)
admin.site.register(Vote)
