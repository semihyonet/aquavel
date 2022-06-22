from django.apps import AppConfig


class CustomAuthConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'custom_auth'

    def ready(self):
        # Implicitly connect a signal handlers decorated with @receiver.
        from . import signals

