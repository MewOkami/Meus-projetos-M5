from django.db import models
from uuid import uuid4
from django.db.models import UUIDField


class CourseStatus(models.TextChoices):
    PENDING = "pending"
    ACCEPTED = "accepted"


class StudentCourse(models.Model):
    id = UUIDField(primary_key=True, editable=False, default=uuid4)
    name = models.TextField()
    status = models.CharField(
        max_length=11,
        choices=CourseStatus.choices, default=CourseStatus.PENDING)
    course = models.ForeignKey(
        "courses.Course",
        on_delete=models.CASCADE,
        related_name="students_courses"
    )
    student = models.ForeignKey(
        "accounts.Account",
        on_delete=models.CASCADE,
        related_name="students_courses"
    )
