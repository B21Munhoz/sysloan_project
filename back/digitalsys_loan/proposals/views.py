from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from proposals.serializers import ProposalSerializer, FormStructure
from django.db import transaction
from proposals.tasks import process_proposal_task
# Create your views here.

headers= {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Credentials": True,
  "Access-Control-Allow-Headers": "Origin,Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token,locale",
  "Access-Control-Allow-Methods": "GET, POST, HEADERS, OPTIONS"
}

class ProposalView(APIView):
    def post(self, request): 
        serializer = ProposalSerializer(data=request.data)
        if serializer.is_valid():
            instance = serializer.save()
            instance.save()
            # Após salvar no banco, enviamos para a queue do Celery.
            task_params = {'id': instance.id}
            transaction.on_commit(lambda: process_proposal_task.delay(task_params))
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST, headers=headers)


class FormStructureView(APIView):
    def get(self, request):
        structure = FormStructure.load()
        return Response({
            "fields": structure.proposal_fields
        }, status=status.HTTP_200_OK, headers=headers
        )