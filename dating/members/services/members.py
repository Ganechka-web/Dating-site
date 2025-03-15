from django.contrib.auth import get_user_model
from django.http.request import QueryDict
from django.db.models import QuerySet


DatingUser = get_user_model()


def get_members_without_cur_user(cuu_user_id: int) -> QuerySet:
    return DatingUser.objects.exclude(id=cuu_user_id)


def filter_members(members: QuerySet, params: QueryDict) -> QuerySet:
    """Filters user according to params"""
    filters = {'is_active': True}

    if params.get('gender') and params['gender'] != 'UNK':
        filters['gender'] = params['gender']
    if params.get('interests'):
        filters['interests__in'] = params.getlist('interests')
    if params.get('min_age'):
        filters['age__gte'] = params['min_age']
    if params.get('max_age'):
        filters['age__lte'] = params['max_age']
    if params.get('cities'):
        filters['city__in'] = params.getlist('cities')

    return members.filter(**filters).distinct()