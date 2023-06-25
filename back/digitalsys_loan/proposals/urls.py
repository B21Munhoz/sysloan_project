from django.urls import path
from proposals.views import ProposalView, FormStructureView

proposals_urlpatterns = [
    path('send_proposal/', ProposalView.as_view()),
    path('get_form_fields/', FormStructureView.as_view()),
]