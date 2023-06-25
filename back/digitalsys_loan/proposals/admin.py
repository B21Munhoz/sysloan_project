from django.contrib import admin
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin
from proposals.models import FormStructure, Proposal

# Usando o pacote django_better_admin_arrayfield, assim temos uma interface mais amigável
# para editar a lista de fields de uma Proposal.

class FormStructureAdmin(admin.ModelAdmin, DynamicArrayMixin):
    # Dando um Override no método que renderiza o form.
    # Como é um Singleton, não quero poder deletá-lo, nem adicionar outro.
    def render_change_form(self, request, context, add=False, change=True, form_url='', obj=None):
        context.update({
            'show_save': True,
            'show_save_and_continue': True,
            'show_save_and_add_another': False,
            'show_delete': False
        })
        return super().render_change_form(request, context, add, change, form_url, obj)
    
    # Dando um Override no método de permissão para adição do objeto.
    # Como é um Singleton, só quero essa opção se não houver um FormStructure criado.
    def has_add_permission(self, request):
        if self.model.objects.count() > 0:
            return False
        else:
            return True


class ProposalAdmin(admin.ModelAdmin):
    list_display = ['cpf','answer', 'created']


admin.site.register(FormStructure, FormStructureAdmin)
admin.site.register(Proposal, ProposalAdmin)