from django.db.models.signals import pre_save
from django.dispatch import receiver

from custom_auth.models import CustomUser
from custom_auth.helpers import encrypt


@receiver(pre_save, sender=CustomUser)
def encryptPassword(sender, instance, *args, **kwargs):
    instance.password = encrypt(instance.password)

