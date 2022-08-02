import os
import binascii
from datetime import datetime, timedelta, timezone
from random import random
import pytz

from django.db import models
from django.utils import timezone

from rest_framework.authtoken.models import Token

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


class UniqueToken(models.Model):
    """
    TODO: Add doc string
    """
    class Meta:
        abstract = True

    key = models.CharField(max_length=80)
    created_date = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    @classmethod
    def generate_key(cls):
        return binascii.hexlify(os.urandom(round((random() + 1) * 20))).decode()

    def save(self, *args, **kwargs):
        self.key = self.generate_key()
        return super().save(*args, **kwargs)


class EmailVerificationToken(UniqueToken):
    """
    TODO: Add doc string
    """
    
    class Meta:
        default_related_name = 'email_verification_token'

    def verify_email(self) -> None:
        # Set the user's email address as verified
        self.user.email_verified = True
        self.user.email_verified_date = datetime.now(tz=pytz.utc)
        self.user.save()

        # Delete the email verification token used to authenticate the user
        self.delete()


class ResetPasswordToken(UniqueToken):

    class Meta:
        default_related_name = 'reset_password_token'
