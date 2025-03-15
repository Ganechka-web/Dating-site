from django.db.models import QuerySet
from django.contrib.auth import get_user_model
from django.utils import timezone

from recommendations.conversation import AiHelper
from recommendations.models import Recommendation 


DatingUser = get_user_model()


def create_recommendation(asker_id: int, target_id: int) -> None: 
    """
    Creates recommendation according to two users from db
    and adds it to foreign key   
    """
    asker = DatingUser.objects.get(id=asker_id)
    target = DatingUser.objects.get(id=target_id)

    helper = AiHelper(asker, target)
    answer = helper.get_helper_answer()

    Recommendation.objects.create(asker=asker,
                                  target=target,
                                  content=answer,
                                  asked=timezone.now())
    

def get_user_recommendations(base_queryset: QuerySet, 
                              cur_user_id: int) -> QuerySet:
    return base_queryset.filter(id=cur_user_id) \
                        .select_related('target')
