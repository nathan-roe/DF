from django.db import models
from communication.models.story import Story
from file_storage.models.file import File

class StoryPhoto(File):
    """
    Extends File model to relate to S
    """
    story = models.ForeignKey(Story, related_name='story_photos', on_delete=models.CASCADE)
