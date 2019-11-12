from django.conf import settings
from django.db import models


class Supplier(models.Model):
    name = models.CharField(max_length=255, unique=True)
    logo = models.ImageField(upload_to="supplier", blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    supplier = models.ForeignKey(Supplier, related_name="products", on_delete=models.CASCADE)
    guarantee = models.CharField(max_length=255, blank=True)
    guarantee_des = models.CharField(max_length=255, blank=True)
    name = models.CharField(max_length=255, unique=True)
    color = models.CharField(max_length=255, blank=True)
    screen = models.CharField(max_length=255, blank=True)
    resolution = models.CharField(max_length=255, blank=True)
    front_camera = models.CharField(max_length=255, blank=True)
    rear_camera = models.CharField(max_length=255, blank=True)
    chip = models.CharField(max_length=255, blank=True)
    ram = models.CharField(max_length=255, blank=True)
    rom = models.CharField(max_length=255, blank=True)
    pin = models.CharField(max_length=255, blank=True)
    operating_system = models.CharField(max_length=255, blank=True)
    charging_port = models.CharField(max_length=255, blank=True)
    retail_price = models.IntegerField(default=0, blank=True)
    listed_price = models.IntegerField(default=0)
    promotional_price = models.IntegerField(default=0, blank=True)
    count = models.SmallIntegerField(default=0)
    voting = models.FloatField(default=0, blank=True)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="product", blank=True)
    descript = models.TextField(max_length=255, blank=True)

    def __str__(self):
        return f"self.product"


class Vote(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="votes")
    value = models.SmallIntegerField(default=5)

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
    note = models.TextField(blank=True)
    total = models.BigIntegerField(default=0)

    def __str__(self):
        return f"{self.user} - {self.status}"


class Cart(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.SET_NULL, null=True, blank=True, related_name="carts"
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField(default=0, blank=True)

    def __str__(self):
        return f"{self.user} - {self.product}"


class Import(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    price = models.IntegerField(default=0)
    quantity = models.SmallIntegerField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"self.product"


class Export(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    price = models.IntegerField(default=0)
    quantity = models.SmallIntegerField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"self.product"
