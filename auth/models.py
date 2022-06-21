from django.db import models

# Create your models here.
import core.models


class CustomUser(core.models.AbstractModel):
    username = models.CharField(max_length=64)
    email = models.EmailField(max_length=64)
    password = models.CharField(max_length=64)
