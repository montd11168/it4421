from django.db import models

from apps.users.models import User


class Supplier(models.Model):
    name = models.CharField(max_length=255, unique=True)
    image = models.ImageField(upload_to="supplier", null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    supplier = models.ForeignKey(Supplier, related_name="products", on_delete=models.CASCADE)
    name = models.CharField(max_length=255, unique=True)
    price = models.IntegerField(default=0)
    descript = models.TextField(max_length=255, blank=True)
    count = models.SmallIntegerField(default=0)
    image = models.ImageField(upload_to="product", null=True, blank=True)

    def __str__(self):
        return f"{self.supplier} {self.name}"


class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="votes")
    value = models.SmallIntegerField()

    class Meta:
        unique_together = ['user', 'product']

    def __str__(self):
        return f"{self.user}-{self.product}"


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()

    def __str__(self):
        return f"{self.user}-{self.product}"
