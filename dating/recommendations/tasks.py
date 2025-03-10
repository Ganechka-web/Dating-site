from celery import shared_task

from recommendations.services.recommendations import create_recommendation


@shared_task(ignore_result=True, time_limit=60 * 30)
def process_recommendation(asker_id: int, target_id: int) -> None:
    """Calls recommendation service to create a recommendation"""
    create_recommendation(asker_id, target_id)
