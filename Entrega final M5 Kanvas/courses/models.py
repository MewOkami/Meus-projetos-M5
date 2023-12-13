from django.db import models
from uuid import uuid4
from django.db.models import UUIDField


class Course_status(models.TextChoices):
    NOT_STARTED = "not started"
    IN_PROGRESS = "in progress"
    FINISHED = "finished"


class Course(models.Model):
    id = UUIDField(primary_key=True, editable=False, default=uuid4)
    name = models.CharField(max_length=100, unique=True)
    status = models.CharField(
        max_length=11,
        choices=Course_status.choices,
        default=Course_status.NOT_STARTED
    )
    start_date = models.DateField()
    end_date = models.DateField()
    instructor = models.ForeignKey(
        "accounts.Account",
        on_delete=models.CASCADE,
        related_name="courses",
        null=True
    )
    students = models.ManyToManyField(
        "accounts.Account",
        related_name="my_courses",
        through="students_courses.StudentCourse"
    )
