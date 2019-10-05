from django.conf import settings
from django.db import models


class Supplier(models.Model):
    name = models.CharField(max_length=255, unique=True)
    logo = models.ImageField(upload_to="supplier", blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    supplier = models.ForeignKey(Supplier, related_name="products", on_delete=models.CASCADE)
    name = models.CharField(max_length=255, unique=True)
    descript = models.TextField(max_length=255, blank=True)
    operating_system = models.CharField(max_length=255, blank=True)
    ram = models.CharField(max_length=255, blank=True)
    rom = models.CharField(max_length=255, blank=True)
    battery = models.CharField(max_length=255, blank=True)
    front_camera = models.CharField(max_length=255, blank=True)
    rear_camera = models.CharField(max_length=255, blank=True)
    sim = models.CharField(max_length=255, blank=True)
    screen = models.CharField(max_length=255, blank=True)
    memory_card = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.supplier} {self.name}"


class ProductColor(models.Model):
    product = models.ForeignKey(Product, related_name="colors", on_delete=models.CASCADE)
    color = models.CharField(max_length=45, unique=True)
    price = models.IntegerField(default=0)
    count = models.SmallIntegerField(default=0)

    def __str__(self):
        return f"{self.color}"


class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="product", blank=True)
    descript = models.TextField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.product}"


class Vote(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="votes")
    value = models.SmallIntegerField()

    class Meta:
        unique_together = ["user", "product"]

    def __str__(self):
        return f"{self.user} - {self.product}"


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField(blank=True)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.product}"


class Order(models.Model):
    STATUS_CHOICES = [
        ("XÁC NHẬN", "Xác nhận"),
        ("ĐANG GIAO", "Đang giao"),
        ("ĐÃ GIAO", "Đã giao"),
        ("ĐÃ HỦY", "Đã hủy"),
        ("TRẢ HÀNG", "Trả hàng"),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=9, choices=STATUS_CHOICES, default="XÁC NHẬN")

    def __str__(self):
        return f"{self.user} - {self.status}"


class Item(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField()

    def __str__(self):
        return f"{self.product} - {self.quantity}"


class Import(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    price = models.IntegerField(default=0)
    quantity = models.SmallIntegerField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product} - {self.quantity}"


class Export(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    price = models.IntegerField(default=0)
    quantity = models.SmallIntegerField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product} - {self.quantity}"
