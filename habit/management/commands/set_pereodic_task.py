from django.core.management import BaseCommand

from datetime import datetime, timedelta

from django_celery_beat.models import PeriodicTask, IntervalSchedule


class Command(BaseCommand):
    def handle(self, *args, **options):
        schedule, created = IntervalSchedule.objects.get_or_create(every=60, period=IntervalSchedule.SECONDS, )
        if 'message_tg' not in [i.name for i in PeriodicTask.objects.all()]:
            PeriodicTask.objects.create(interval=schedule, name="message_tg", task='config.tasks.check_time_to_send',
                                        expires=datetime.utcnow() + timedelta(seconds=30))
