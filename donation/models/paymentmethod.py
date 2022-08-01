from django.db import models
from safedelete.models import SafeDeleteModel


class PaymentMethod(SafeDeleteModel):
    """
    TODO: Add doc string
    """
    class Meta:
        abstract = True

    payment_id = models.CharField(max_length=255)

    class PaymentType(models.IntegerChoices):
        CARD = 1, 'Card'
        PAYPAL = 2, 'Paypal'

    payment_type = models.IntegerField(choices=PaymentType.choices, default=PaymentType.CARD)

    
    def __str__(self) -> str:
        return f'Payment ID: {self.payment_id} | Payment Type: {self.payment_type}'
