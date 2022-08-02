from datetime import datetime, timezone

from rest_framework import exceptions
from rest_framework.authentication import TokenAuthentication

from df_auth.models.tokens import ExpiringToken


class ExpiringTokenAuthentication(TokenAuthentication):
    """Extends default token auth to be time based."""

    model = ExpiringToken

    class Meta:
        default_related_name = 'expiring_token'

    def authenticate_credentials(self, key):        
        try:
            token = self.model.objects.get(key=key)
        except self.model.DoesNotExist:
            raise exceptions.AuthenticationFailed('Invalid token')

        if not token.user.is_active or token.user.deleted is not None:
            raise exceptions.AuthenticationFailed('User inactive or deleted')

        if token.expired:
            raise exceptions.AuthenticationFailed('Token has expired')
        
        # Reset the created time of the token to now.
        token.created = datetime.now(timezone.utc)
        token.save()

        return (token.user, token)
