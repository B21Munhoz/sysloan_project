from django.db import models
from django_better_admin_arrayfield.models.fields import ArrayField
from utils.pattern_models import SingletonModel
from django.utils import timezone

# Create your models here.


class FormStructure(SingletonModel):
    # Model para salvar a estrutura do formulário da proposta.
    # Por ser um Singleton criado automaticamente se não houver uma instância
    # no DB, será criado com 3 campos default.
    proposal_fields = ArrayField(
            models.CharField(max_length=20, blank=True),
            default = list(['name', 'address', 'value']) 
        )


ANSWER_CHOICES = (
    ('Pendente', 'Pendente'),
    ('Aprovada', 'Aprovada'),
    ('Negada', 'Negada')
)


class Proposal(models.Model):
    # Model para salvar as propostas dos usuários.
    # Sempre será necessário pelo menos o CPF.
    # Proposal info irá receber um JSON com as informações
    # estabelecidas no FormStructure
    proposal_info = models.JSONField(null=True)
    cpf = models.CharField(max_length=12, verbose_name='CPF')
    created = models.DateTimeField(default=timezone.now(), verbose_name='Data de Criação')
    answer = models.CharField(
        max_length = 20,
        choices = ANSWER_CHOICES,
        default = 'Pendente',
        verbose_name='Resposta'
    )
        