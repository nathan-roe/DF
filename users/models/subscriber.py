from django.db import models
from users.models.user import User
from donation.models.paymentmethod import PaymentMethod


class Subscriber(User, PaymentMethod):
    """
    TODO: Add doc string
    """
    send_email_notifications = models.BooleanField(default=True)
    send_sms_notifications = models.BooleanField(default=True)
    opt_in_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)


    def __str__(self) -> str:
        return f'{super().__str__()} | state: {self.state} | city: {self.city} | address: {self.address}'
