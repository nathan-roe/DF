import uuid

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from safedelete.models import SafeDeleteModel, HARD_DELETE_NOCASCADE

from users.managers.usermanager import UserManager
from users.utility.validators import USER_NAME_VALIDATOR


class User(AbstractBaseUser, PermissionsMixin, SafeDeleteModel):
    """
    TODO: Add doc string
    """
    _safedelete_policy = HARD_DELETE_NOCASCADE

    USERNAME_FIELD = 'email_address'
    EMAIL_FIELD = 'email_address'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_number']
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    first_name = models.CharField(validators=[USER_NAME_VALIDATOR], max_length=50)
    last_name = models.CharField(validators=[USER_NAME_VALIDATOR], max_length=50)
    email_address = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=255)
    email_verified = models.BooleanField(default=False)
    email_verified_date = models.DateTimeField(blank=True, null=True)
    is_admin = models.BooleanField(default=False)
    is_locked = models.BooleanField(default=False)

    objects = UserManager()


    @property
    def full_name(self) -> str:
        return f'{self.first_name} {self.last_name}'

    def __str__(self) -> str:
        return f'ID: {self.id} | name: {self.first_name} {self.last_name}'\
            f'| email: {self.email_address} | phone: {self.phone_number}'
