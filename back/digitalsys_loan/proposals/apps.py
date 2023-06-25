from django.apps import AppConfig
from django.db.models.signals import post_migrate


# class ProposalsConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'proposals'
#     def ready(self) -> None:
#         def create_form_structure(sender, **kwargs):
#             from proposals.models import FormStructure
#             if not FormStructure.objects.filter(id=1).exists():
#                 FormStructure.load()
#         post_migrate.connect(create_form_structure ,sender=self)