from rest_framework import serializers
from users.models.recipient import Recipient
from users.serializers.userserializers import UserCreationMixin


class RecipientAllSerializer(UserCreationMixin, serializers.ModelSerializer):
    """Serializer used for handling all fields of the Recipient model"""

    class Meta:
        model = Recipient
        fields = '__all__'
