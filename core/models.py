from django.db import models

# Create your models here.


class AbstractModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    deleted_at = models.DateTimeField()

    class Meta:
        abstract = True
