from celery import shared_task
from datetime import datetime

from habit.models import Habit
from overall.services import message_send, get_chat_id


@shared_task
def check_time_to_send():
    for obj in Habit.objects.all():
        time_now = datetime.now().replace(microsecond=False).time()

        if obj.time <= time_now and time_now > obj.last_send.replace(tzinfo=None).time():

            obj.last_send = time_now
            if obj.owner.tg_chat_id:
                message_send(time=obj.time, owner=obj.owner, place=obj.place, action=obj.action,
                             chat_id=obj.owner.tg_chat_id)
            else:
                chat_id = get_chat_id(obj.owner.tg_username, obj.owner.id)
                message_send(time=obj.time, owner=obj.owner, place=obj.place, action=obj.action,
                             chat_id=chat_id)
