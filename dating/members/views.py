from django.views.generic.base import View, TemplateResponseMixin

from .forms import FilterMembersForm


class MembersListView(View, TemplateResponseMixin):
    template_name = 'members/member/list.html'

    def get(self, request):
        form = FilterMembersForm(request.GET)

        return self.render_to_response({'filter_form': form})
