from django.db import models
from safedelete.models import SafeDeleteModel

from users.models.user import User


class Communication(SafeDeleteModel):
    """
    Model used for keeping track of communications between users.
    """
    user = models.ForeignKey(User, related_name='communications', on_delete=models.CASCADE)
    sent_date = models.DateTimeField(auto_now_add=True)
    
    class CommunicationType(models.IntegerChoices):
        EMAIL = 1, 'Email'
        SMS = 2, 'SMS'

    communication_type = models.IntegerField(choices=CommunicationType.choices, default=CommunicationType.EMAIL)

    class MessageType(models.IntegerChoices):
        SUBMITTED_TO_SEEN = 1, 'Updated Submitted Status to Seen'
        SEEN_TO_PENDING = 2, 'Updated Seen Status to Pending'
        PENDING_TO_APPROVED = 3, 'Updated Pending Status to Approved'
        PENDING_TO_DECLINED = 4, 'Updated Pending Status to Declined'
        DECLINED_TO_APPROVED = 5, 'Updated Declined Status to Approved'
        APPROVED_TO_DECLINED = 6, 'Updated Approved Status to Declined'

    message_type = models.IntegerField(choices=MessageType.choices, default=MessageType.SUBMITTED_TO_SEEN)
