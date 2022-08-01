from django.db import models
from communication.models.story import Story
from file_storage.models.file import File

class StoryPhoto(File):
    """
    TODO: Add doc string
    """
    story = models.ForeignKey(Story, related_name='story_photos')