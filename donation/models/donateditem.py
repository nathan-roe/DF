from django.db import models
from safedelete.models import SafeDeleteModel
from users.models.recipient import Recipient

class DonationItem(SafeDeleteModel):
    """
    TODO: Add doc string
    """
    name = models.CharField(max_length=255)
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    recipient = models.ForeignKey(Recipient, related_name='donation_items')
    
    class StatusTypes(models.IntegerChoices):
        SUBMITTED = 1, 'Submitted'
        SEEN = 2, 'Seen'
        PENDING = 3, 'Pending'
        APPROVED = 4, 'Approved'
        DECLINED = 5, 'Declined'

    status = models.IntegerField(choices=StatusTypes.choices, default=StatusTypes.SUBMITTED)
