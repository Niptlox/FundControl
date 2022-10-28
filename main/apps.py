from django.apps import AppConfig


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'

    def ready(self):
        from main.models import standard_groups
        from main.models import FinanceGroup

        for name in standard_groups:
            if not FinanceGroup.objects.filter(name=name).all():
                FinanceGroup(name=name).save()
