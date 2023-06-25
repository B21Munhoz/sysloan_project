from rest_framework import serializers
from proposals.models import Proposal, FormStructure
from rest_framework.exceptions import APIException
from rest_framework import status

class ProposalFieldsValidationError(APIException):
    status_code=status.HTTP_400_BAD_REQUEST


class ProposalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proposal
        fields = ["cpf", "proposal_info"]
    
    proposal_info = serializers.JSONField

    def validate_proposal_info(self, proposal_info):
        # Aqui realizamos a validação dos campos customizados do formulário,
        # contidos no campo proposal_fields.
        structure = FormStructure.load()
        if proposal_info in [{}, None]:
            raise ProposalFieldsValidationError(detail="Field 'proposal'_info is needed")

        for key in structure.proposal_fields:
            if key not in proposal_info:
                raise ProposalFieldsValidationError(detail=f"Field '{key}' is needed")