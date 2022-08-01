from functools import cached_property
from django.db import models
from file_storage.functions import b64_to_fileobj, delete_file, get_file_url, upload_file
from safedelete.models import SafeDeleteModel


class File(SafeDeleteModel):
    """
    TODO: Add doc string
    """

    class Meta:
        abstract = True
    
    file_path = models.CharField(max_length=255, null=True, blank=True)

    @cached_property
    def file_url(self):
        """
        TODO: Add doc string
        """
        return get_file_url(self.file_path)

    def update_or_delete(self, file, new_file_path):
        """
        TODO: Add doc string
        """
        # Update file.
        if file:
            delete_file(self.file_path)
            upload_file(new_file_path, b64_to_fileobj(file))
            self.file_path = new_file_path
            self.save()
        #  Self-destruct.
        else:
            self.delete()

    def delete(self, *args, **kwargs):
        """Method used to remove S3 file from AWS before deletion"""
        delete_file(self.file_path)
        super().delete(*args, **kwargs)

    def __str__(self) -> str:
        return f'{self.file_path} | ID: {self.id}'
