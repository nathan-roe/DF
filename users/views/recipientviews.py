from django.db import transaction

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from users.serializers.recipientserializers import RecipientAllSerializer
from users.utility.functions import send_verificiation_email, verify_user

from util.constants import Constants


class RecipientSignUpView(APIView):
    """
    View for creating a recipient account.
    """
    def post(self, request):
        """
        Method used to create a Recipient instance
        Expected POST Data:
        {
            "first_name": str,
            "last_name": str,
            "email_address": str,
            "phone_number": str (optional),
            "password": str,
            "recaptcha_key": str
        }
        """
        with transaction.atomic():
            
            recipient_data = request.data

            # Validate reCaptcha key, email address and raises error if invalid
            verify_user(request, recipient_data)

            recipient_data['email_address'] = recipient_data['email_address'].lower()

            recipient_serializer = RecipientAllSerializer(data=recipient_data)
            recipient_serializer.is_valid()
            recipient = recipient_serializer.save()

            send_verificiation_email(recipient, Constants.EmailVerificationType.RECIPIENT_VERIFICATION)

            return Response(recipient_serializer.data, status=status.HTTP_201_CREATED)
