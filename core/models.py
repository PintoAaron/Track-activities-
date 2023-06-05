from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    emaail = models.EmailField(unique=True)
