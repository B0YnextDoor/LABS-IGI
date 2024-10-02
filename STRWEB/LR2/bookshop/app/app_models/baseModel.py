from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    id = models.BigAutoField(
        auto_created=True, primary_key=True, help_text="Unique ID")
    created_at = models.DateTimeField(
        default=timezone.now, help_text='Creation date & time')
    updated_at = models.DateTimeField(
        default=timezone.now, help_text='Last update date & time')

    class Meta:
        abstract = True
