from django.apps import AppConfig


class CountdownAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'countdown_app'

    def ready(self):
        import countdown_app.signals