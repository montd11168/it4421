from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
import binascii
import os

from django.conf import settings


class Token(models.Model):
    key = models.CharField(_("Key"), max_length=40, primary_key=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="tokens",
        on_delete=models.CASCADE,
        verbose_name=_("User"),
    )
    created = models.DateTimeField(_("Created"), auto_now_add=True)

    class Meta:
        verbose_name = _("Token")
        verbose_name_plural = _("Tokens")

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        return super().save(*args, **kwargs)

    def generate_key(self):
        return binascii.hexlify(os.urandom(20)).decode()

    def __str__(self):
        return self.key


class User(AbstractUser):
    GENDER_CHOICES = [("NAM", "Nam"), ("NỮ", "Nữ"), ("KHÁC", "Khác")]
    email = models.EmailField(_("email address"), unique=True)
    username = models.CharField(max_length=50, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    address = models.TextField(blank=True)
    gender = models.CharField(max_length=9, choices=GENDER_CHOICES, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email
