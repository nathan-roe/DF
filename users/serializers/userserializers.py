from rest_framework import serializers


class UserCreationMixin(metaclass=serializers.SerializerMetaclass):
    """
    Serializer mixin used in model serializers related to the User model.
    Handles the creation of a User instance. 
    """
    def create(self, validated_data):
        """
        Handles the creation of a User instance through the UserManageer model
        """
        return self.Meta.model.objects.create_user(**validated_data)
