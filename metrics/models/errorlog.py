from django.db import models
from users.models.user import User


class ErrorLog(models.Model):
    """
    TODO: Add doc string
    """
    user = models.ForeignKey(User, related_name='error_logs', null=True, blank=True),
    error_traceback = models.CharField(max_length=255),
    url_path = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f'ID: {self.id} | User: {self.user} | URL path: {self.url_path}'
