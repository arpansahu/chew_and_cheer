from django.apps import AppConfig


class CruddjangoformConfig(AppConfig):
    name = 'cruddjangoform'

    def ready(self):
        import cruddjangoform.signals
