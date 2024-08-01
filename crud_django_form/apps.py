from django.apps import AppConfig


class crud_django_formConfig(AppConfig):
    name = 'crud_django_form'

    def ready(self):
        import crud_django_form.signals
