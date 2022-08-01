from django.db import models
from safedelete.models import SafeDeleteModel

from users.models.recipient import Recipient


class Story(SafeDeleteModel):
    """
    TODO: Add doc string
    """
    recipient = models.ForeignKey(Recipient, related_name="stories", null=True, blank=True)
    summary = models.TextField(max_length=5000)

    def __str__(self) -> str:
        return f'ID: {self.id} Recipient: {self.recipient}'
