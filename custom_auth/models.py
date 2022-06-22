from django.db import models


from core.models import AbstractUserModel


class CustomUser(AbstractUserModel):
    def __str__(self):
        return self.username
