from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4
from django.db.models import UUIDField


class Account(AbstractUser):
    id = UUIDField(primary_key=True, editable=False, default=uuid4)
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    email = models.EmailField(max_length=100, unique=True)
    is_superuser = models.BooleanField(blank=True, default=False)
