from django.utils.decorators import method_decorator
from django.views.generic.base import View, TemplateResponseMixin
from django.views.generic import DetailView
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from django.db.models import QuerySet

from members.services.members import get_members_without_cur_user, \
                                        filter_members
from .forms import FilterMembersForm


DatingUser = get_user_model()


@method_decorator(login_required, name='dispatch')
class MembersListView(View, TemplateResponseMixin):
    """Filters or give all members"""
    template_name = 'members/member/list.html'

    def get(self, request):
        form = FilterMembersForm(request.GET)
        members: QuerySet

        members_key: str = "members:exclude:{}".format(request.user.id)
        members = cache.get(members_key)
        if members is None:
            members = get_members_without_cur_user(request.user.id)
            cache.set(members_key, members, timeout=60*10)

        if request.GET:
            # get cache from url parms
            members_filter_key = request.GET.urlencode()
            members = cache.get(members_filter_key) 
            if members is None:
                members = filter_members(members, request.GET)
                cache.set(members_filter_key, members, timeout=60*5)

        return self.render_to_response({'section': 'members',
                                        'filter_form': form,
                                        'members': members})


class MemberDetailView(DetailView):
    """Sends html template of detail user page to js fetch"""
    template_name = 'members/member/detail.html'
    model = DatingUser

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['section'] = 'members'

        return context
    
    def get_object(self, queryset: QuerySet | None) -> DatingUser:
        member: DatingUser
        pk = self.kwargs.get(self.pk_url_kwarg)

        if queryset is None:
            queryset = self.get_queryset()

        member_key = 'member:{}'.format(pk)
        member = cache.get(member_key)
        if member is None:
            member = queryset.get(pk=pk)
            cache.set(member_key, member, 60*10)

        return member
    