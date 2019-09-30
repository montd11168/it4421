from django.contrib import admin

from .models import Cart, Comment, Order, Product, Supplier, Vote

# Register your models here.

admin.site.register(Supplier)
admin.site.register(Product)
admin.site.register(Vote)
admin.site.register(Comment)
admin.site.register(Cart)
admin.site.register(Order)
