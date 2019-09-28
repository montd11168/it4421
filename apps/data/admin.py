from django.contrib import admin

from .models import Comment, Product, Supplier, Vote

# Register your models here.

admin.site.register(Supplier)
admin.site.register(Product)
admin.site.register(Vote)
admin.site.register(Comment)
