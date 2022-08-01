from django.db import models
from donation.models.paymentmethod import PaymentMethod
from users.models.subscriber import Subscriber


class FinancialDonation(PaymentMethod):
    """
    TODO: Add doc string
    """
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    subscriber = models.ForeignKey(Subscriber, related_name='financial_donations', null=True, blank=True)

    def __str__(self) -> str:
        return f'{super().__str__()} | amount: {self.amount}'
