from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.views.generic import ListView, DetailView
from django.utils.decorators import method_decorator
from django.http import JsonResponse, HttpRequest
from django.db.models import QuerySet
from django.core.cache import cache

from recommendations.services.recommendations import \
    get_user_recommendations
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
        
        # delete old cache data
        user_recommendations_key = 'recommendations:user:{}' \
                                   .format(request.user.id)
        user_recommendations = cache.get(user_recommendations_key)
        if user_recommendations:
            cache.delete(user_recommendations_key)

        return JsonResponse({'status': 'ok'})
    return JsonResponse({'status': 'error'})


@method_decorator(decorator=login_required, name='dispatch')
class RecommendationsListView(ListView):
    template_name = 'recommendations/recommendation/list.html'
    model = Recommendation
    context_object_name = 'recommendations'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['section'] = 'recommendations'

        return context
    
    def get_queryset(self):
        user_recommendations: QuerySet

        user_recommendations_key = 'recommendations:user:{}' \
                                   .format(self.request.user.id)
        user_recommendations = cache.get(user_recommendations_key)
        if user_recommendations:
            return user_recommendations
        
        user_recommendations = get_user_recommendations(
            super().get_queryset(),
            self.request.user.id)
        cache.set(user_recommendations_key, user_recommendations, 
                    timeout=60*10)
            
        return user_recommendations
    

@method_decorator(decorator=login_required, name='dispatch')
class RecommendationsDetailView(DetailView):
    template_name = 'recommendations/recommendation/detail.html'
    model = Recommendation
    context_object_name = 'recommendation'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['section'] = 'recommendations'

        return context
    
    def get_object(self, queryset = ...):
        user_recommendation: Recommendation
        pk = self.kwargs[self.pk_url_kwarg]

        user_recommendation_key = 'recommendation:user:{}'.format(pk)
        user_recommendation = cache.get(user_recommendation_key)
        if user_recommendation:
            return user_recommendation
        
        user_recommendation = queryset.get(pk=pk)
        cache.set(user_recommendation_key, user_recommendation,
                  timeout=60*5)
        