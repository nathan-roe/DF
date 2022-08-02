from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from df_auth.models.tokens import EmailVerificationToken


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
        token_key = request.data['verification_token']
        token = get_object_or_404(EmailVerificationToken, token_key=token_key)
        token.verify_email()

        return Response({'message': 'Email verified'}, status=status.HTTP_202_ACCEPTED)
