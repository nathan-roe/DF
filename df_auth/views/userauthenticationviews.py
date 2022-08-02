from datetime import timedelta
from django.utils import timezone
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken

from df_auth.models.accesslog import AccessLog
from df_auth.models.tokens import EmailVerificationToken, ExpiringToken

from users.models.user import User

from util.constants import Constants


class EmailVerificationView(APIView):
    """
    View used to verify a user's email address
    """
    def post(self, request):
        """
        Method used to verify a User instance
        Expected POST Data:
        {
            "verification_token": str 
        }
        """
        key = request.data['verification_token']
        token = get_object_or_404(EmailVerificationToken, key=key)
        token.verify_email()

        return Response({'message': 'Email verified'}, status=status.HTTP_202_ACCEPTED)


class ExpiringAuthTokenView(ObtainAuthToken):
    """
    View used to verify a user's email address
    """
    authentication_classes = []
    model = ExpiringToken

    def post(self, request):
        """
        Method used to verify a User instance
        Expected POST Data:
        {
            "email_address": str,
            "password": str
        }
        """
        user_data = request.data

        token_serializer = AuthTokenSerializer(data={
            'username': user_data['email_address'],
            'password': user_data['password']
        })

        # Handle authorization errors
        last_login_attempt = timezone.now() - timedelta(seconds=Constants.LoginConstants.LOGIN_THROTTLE)
        throttled_login_attempts = AccessLog.objects.filter(access_date__gte=last_login_attempt,
                                                            attempt_successful=False).count()

        if throttled_login_attempts > Constants.LoginConstants.MAX_LOGIN_REQUESTS:
            return Response(status=status.HTTP_429_TOO_MANY_REQUESTS)
        elif User.objects.filter(email_address=user_data['email_address'], is_locked=True).exists():
            return Response(status=status.HTTP_403_FORBIDDEN)
        
        access_log = AccessLog.objects.create(attempt_email=user_data['email_address'],
                                              action_type=AccessLog.ActionType.LOGIN)

        # Login user
        if User.objects.filter(email_address=user_data['email_address'], deleted=None).exists() \
                and token_serializer.is_valid() \
                and token_serializer.validated_data['user'].email_verified:
            
            cur_user = User.objects.get(email_address=user_data['email_address'])

            # Delete auth tokens if they exist
            if (exp_tokens := ExpiringToken.objects.filter(user=cur_user)).count() > 0:
                exp_tokens.delete()
            # Create new auth token
            token = ExpiringToken.objects.create(user=cur_user)

            # Update AccessLog
            access_log.success_user = token_serializer.validated_data['user']
            access_log.attempt_successful = True
            access_log.save()
            
            # Return the authentication token to front end for cookie storage.
            return Response({'token': token.key}, status=status.HTTP_200_OK)

        attempts_in_thirty_minutes = AccessLog.objects.filter(access_date__gte=timezone.now() - timedelta(minutes=30))

        if attempts_in_thirty_minutes.filter(attempt_successful=False).count() >= Constants.LoginConstants.MAX_FAILED_LOGINS \
                and attempts_in_thirty_minutes.filter(attempt_successful=True).count() == 0:
            try:
                user = User.objects.get(email_address=user_data['email_address'])
                user.is_locked = True
                user.save()
            except User.DoesNotExist:
                pass

        return Response(status=status.HTTP_401_UNAUTHORIZED)
