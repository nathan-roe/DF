from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from df_auth.models import ExpiringTokenAuthentication as TokenAuthentication

from donation.models.donationitem import DonationItem
from donation.serializers.donationitemserializers import DonationItemAllSerializer, \
    DonationItemListSerializer

from util.functions import token_to_userprofile


class DonationRequestView(APIView):
    """
    View for handling recipient user item requests.
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


    def get(self, request):
        """
        Method for returning a list of the requested items from a Recipient user.
        """
        user = token_to_userprofile(request)

        donation_items = DonationItem.objects.filter(recipient=user.recipient)
        serializer = DonationItemListSerializer(donation_items, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request):
        """
        Method for requesting an item. Creates a DonationItem object and attaches it to the account.
        Expected POST Data:
        {
            "name": str,
            "estimated_cost": float,
            "link_to_item": url str (optional)
            "reason": str
        }
        """
        user = token_to_userprofile(request)

        donation_item_serializer = DonationItemAllSerializer(data={**request.data, 'recipient': user.recipient})
        donation_item_serializer.is_valid(raise_exception=ValueError)
        donation_item_serializer.save()

        return Response({'message': 'Successfully sent an item request'}, status=status.HTTP_201_CREATED)
