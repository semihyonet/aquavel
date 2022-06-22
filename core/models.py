from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class AbstractModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    deleted_at = models.DateTimeField(null=True)

    class Meta:
        abstract = True

class AbstractUserModel(AbstractUser):
    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    deleted_at = models.DateTimeField(null=True)

    class Meta:
        abstract = True
