from rest_framework import serializers
from users.models.recipient import Recipient


class RecipientAllSerializer(serializers.ModelSerializer):
    """Serializer used for handling all fields of the Recipient model"""

    class Meta:
        model = Recipient
        fields = '__all__'
