from django.views.decorators.http import require_POST
from django.views.generic import ListView
from django.http import JsonResponse, HttpRequest

from .forms import CreateRecommendationForm
from .tasks import process_recommendation
from .models import Recommendation


@require_POST
def create_recommendation(request: HttpRequest) -> JsonResponse:
    """Receives request from js and calls task to create recommendation"""
    form = CreateRecommendationForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        
        process_recommendation.delay(asker_id=request.user.id,
                                     target_id=cd['target_id'])

        return JsonResponse({'status': 'ok'})
    return JsonResponse({'status': 'error'})


class RecommendationsListView(ListView):
    template_name = 'recommendations/recommendation/list.html'
    model = Recommendation

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['section'] = 'recommendations'

        return context
    