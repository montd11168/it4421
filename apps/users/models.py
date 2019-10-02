from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    GENDER_CHOICES = [
        ("NAM", "Nam"),
        ("NỮ", "Nữ"),
        ("KHÁC", "Khác"),
    ]
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(max_length=50, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    address = models.TextField(blank=True)
    gender = models.CharField(max_length=9, choices=GENDER_CHOICES, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    avatar = models.ImageField(upload_to="user", blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email