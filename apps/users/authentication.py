from datetime import timedelta

from django.conf import settings
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from rest_framework import exceptions
from rest_framework.authentication import TokenAuthentication

from .models import Token


class BearerTokenAuthentication(TokenAuthentication):
    keyword = "Bearer"
    model = Token

    def authenticate_credentials(self, key):
        try:
            token = self.model.objects.get(key=key)
        except self.model.DoesNotExist:
            raise exceptions.AuthenticationFailed(_("Invalid token."))

        if not token.user.is_active:
            raise exceptions.AuthenticationFailed(_("User inactive or deleted."))

        is_expired = is_token_expired(token)

        if is_expired:
            raise exceptions.AuthenticationFailed(_("Token has expired"))

        return (token.user, token)


def is_token_expired(token):
    time_elapsed = timezone.now() - token.created
    left_time = timedelta(seconds=settings.TOKEN_EXPIRED_AFTER_SECONDS) - time_elapsed

    return left_time < timedelta(seconds=0)
