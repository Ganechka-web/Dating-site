from django.views.generic.base import View, TemplateResponseMixin
from django.contrib.auth import get_user_model

from .forms import FilterMembersForm


DatingUser = get_user_model()


class MembersListView(View, TemplateResponseMixin):
    template_name = 'members/member/list.html'

    def get(self, request):
        form = FilterMembersForm(request.GET)

        if request.GET:

            filters = {}
            if request.GET.get('interests'):
                filters['interests__in'] = request.GET.getlist('interests')
            if request.GET.get('gender'):
                filters['gender'] = request.GET['gender']
            if request.GET.get('min_age'):
                filters['age__gte'] = request.GET['min_age']
            if request.GET.get('max_age'):
                filters['age__lte'] = request.GET['max_age']
            if request.GET.get('city'):
                filters['city__in'] = request.GET.getlist('cities')

            members = DatingUser.objects.filter(**filters)
            return self.render_to_response({'filter_form': form,
                                            'members': members})



        return self.render_to_response({'filter_form': form})
