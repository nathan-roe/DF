from django.db import models

from users.models.user import User


class AccessLog(models.Model):
    """
    Model used for handling access logs used as validation on sign up and general security logging.
    """

    attempt_email = models.CharField(max_length=255)
    success_user = models.ForeignKey(User, related_name="access_logs", blank=True, null=True, on_delete=models.CASCADE)
    access_date = models.DateTimeField(auto_now_add=True)
    attempt_successful = models.BooleanField(default=False)
    device = models.CharField(max_length=255, blank=True, null=True)
    browser = models.CharField(max_length=255, blank=True, null=True)
    ip_address = models.CharField(max_length=255, blank=True, null=True)

    class ActionType(models.IntegerChoices):
        LOGIN = 1, 'Login'
        LOGOUT = 2, 'Logout'
    
    action_type = models.IntegerField(choices=ActionType.choices, default=ActionType.LOGIN)


    def __str__(self) -> str:
       return f'Action Attempt | {self.date_time} | {self.attempt_user} | \
        {self.get_action_type_display()} | Success: {self.attempt_successful}'
