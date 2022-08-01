from rest_framework import serializers
from file_storage.models import S3File
from file_storage.functions import upload_file
from util.functions import b64_to_fileobj

class FileSerializerMixin(metaclass=serializers.SerializerMetaclass):
    """
    Mixin used for create and update functionality
    """
    def create(self, cleaned_data):
        file = self.context
        if file is None:
            raise ValueError("Context is required")
        upload_file(cleaned_data["file_path"], b64_to_fileobj(file))
        new_s3_file = self.Meta.model.objects.create(**cleaned_data)
        return new_s3_file

    def update(self, instance, validated_data):
        if (file := self.context) is not None and 'file_path' in validated_data:
            instance.update_s3_repo(file, validated_data['file_path'])
        return super().update(instance, validated_data)


class S3FileAllSerializer(FileSerializerMixin, serializers.ModelSerializer):
    """
    Serializer for handling S3File objects with all fields returned
    """
    class Meta:
        model = S3File
        fields = '__all__'


class S3FilePathSerializer(serializers.ModelSerializer):
    """
    Serializer to return s3file path
    """
    class Meta:
        model = S3File
        fields = ['id', 'file_url']
