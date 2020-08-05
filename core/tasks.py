from celery.task import periodic_task
from datetime import timedelta

from core.models import Upvote


@periodic_task(run_every=(timedelta(days=1)), name="reset")
def reset_upvotes_count():
    """
        Reset count of upvotes on all posts once a day.
    """

    Upvote.objects.all().delete()
