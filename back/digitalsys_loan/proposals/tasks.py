from celery import shared_task
import random
from proposals.models import Proposal


@shared_task(queue="proposal_analysis")
def process_proposal_task(task_params):
    # Seguindo a proposta do desafio, toda proposta de empréstimo terá
    # 50% de chance de aprovação, decidida de forma aleatória.
    proposal = Proposal.objects.get(pk=task_params["id"])
    decision = random.choices(['Aprovada', 'Negada'], [1,1])[0] # 2 e 3 são os chars 
    proposal.answer = decision
    proposal.save(force_update=True, update_fields=['answer'])
    return decision
