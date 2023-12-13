from django.db import models
from uuid import uuid4
from django.db.models import UUIDField


class Content(models.Model):
    id = UUIDField(primary_key=True, editable=False, default=uuid4)
    name = models.CharField(max_length=150)
    content = models.TextField()
    video_url = models.CharField(max_length=200, blank=True)
    course = models.ForeignKey(
        "courses.Course",
        on_delete=models.CASCADE,
        related_name="contents"
    )
