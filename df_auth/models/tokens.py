import os
import binascii
from datetime import datetime, timedelta, timezone
from random import random
import pytz

from django.db import models
from django.utils import timezone

from rest_framework import exceptions
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication

from users.models.user import User

TOKEN_EXPIRE_TIME = timedelta(minutes=15)


class ExpiringToken(Token):
    """
    TODO: Add doc string
    """

    class Meta(object):
        proxy=True

    @property
    def expired(self) -> bool:
        """
        TODO: Add doc string
        """
        return self.created < timezone.now() - TOKEN_EXPIRE_TIME


class EmailVerificationToken(models.Model):
    """
    TODO: Add doc string
    """
    token_key = models.CharField(max_length=80)
    created_date = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(User, related_name='email_verification_token', on_delete=models.CASCADE)

    
    def verify_email(self) -> None:
        # Set the user's email address as verified
        self.user.email_verified = True
        self.user.email_verified_date = datetime.now(tz=pytz.utc)
        self.user.save()

        # Delete the email verification token used to authenticate the user
        self.delete()

    @classmethod
    def generate_key(cls):
        return binascii.hexlify(os.urandom(round((random() + 1) * 20))).decode()

    def save(self, *args, **kwargs):
        self.token_key = self.generate_key()
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f'Email Verification Token: {self.user.full_name} | {self.token_key}'


class ExpiringTokenAuthentication(TokenAuthentication):
    """Extends default token auth to be time based."""

    model = ExpiringToken

    def authenticate_credentials(self, key):
        try:
            token = self.model.objects.get(key=key)
        except self.model.DoesNotExist:
            raise exceptions.AuthenticationFailed('Invalid token')

        if not token.user.is_active or token.user.deleted is not None:
            raise exceptions.AuthenticationFailed('User inactive or deleted')

        if token.expired():
            raise exceptions.AuthenticationFailed('Token has expired')
        
        # Reset the created time of the token to now.
        token.created = datetime.now(timezone.utc)
        token.save()

        return (token.user, token)
