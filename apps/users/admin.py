from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .models import User, Token
from django.contrib.auth.forms import UserChangeForm


class TokenAdmin(admin.ModelAdmin):
    list_display = ("user", "created")
    readonly_fields = ("created",)
    search_fields = ("user",)


class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User


class CustomizeUserAdmin(UserAdmin):
    form = MyUserChangeForm
    fieldsets = (
        (None, {"fields": ("username", "password", "verificate_code")}),
        (
            _("Personal info"),
            {"fields": ("email", "phone", "address", "gender", "date_of_birth",)},
        ),
        (
            _("Permissions"),
            {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")},
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = ((None, {"classes": ("wide",), "fields": ("email", "password1", "password2")}),)
    list_display = ("email", "username", "is_active", "is_staff", "is_superuser")
    ordering = ("date_joined",)
    search_fields = ("username", "email")


admin.site.register(Token, TokenAdmin)
admin.site.register(User, CustomizeUserAdmin)
