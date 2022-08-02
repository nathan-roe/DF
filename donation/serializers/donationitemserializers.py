from rest_framework import serializers
from donation.models import DonationItem


class DonationItemAllSerializer(serializers.ModelSerializer):
    """
    Serializer for handling all fields of the DonationItem model
    """
    class Meta:
        model = DonationItem
        fields = '__all__'

class DonationItemListSerializer(serializers.ModelSerializer):
    """
    Serializer for returning fields of the DonationItem model for lists
    """
    class Meta:
        model = DonationItem
        fields = ('id', 'name', 'estimated_cost', 'actual_cost', 'reason', 'link_to_item')
