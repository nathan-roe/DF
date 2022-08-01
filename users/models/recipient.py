from django.db import models
from users.models.user import User


class Recipient(User):
    """
    TODO: Add doc string
    """
    city = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)


    def __str__(self) -> str:
        return f'{super().__str__()} | state: {self.state} | city: {self.city} | address: {self.address}'
