import os

from celery import shared_task, Celery
from datetime import datetime
import requests
from habit.models import Habit
from overall.services import get_chat_id

TOKEN = os.getenv('TG_BOT_TOKEN')
URL = f"https://api.telegram.org/bot{TOKEN}"


@shared_task
def message_send(owner, place, action, time, chat_id):
    param = {
        "chat_id": chat_id,
        "text": f'{owner}, you must do {action} in {place} at {time}'
    }
    requests.get(f'{URL}/sendMessage', params=param)


def check_time_to_send():
    time_now = datetime.now().replace(microsecond=False)
    for obj in Habit.objects.all():
        if obj.last_send:
            if obj.last_send.time() <= time_now.time() and (time_now - obj.last_send.replace(tzinfo=None)).days >= 1:

                obj.last_send = time_now
                obj.save()
                if obj.owner.tg_chat_id:
                    message_send.delay(time=obj.time, owner=obj.owner, place=obj.place, action=obj.action,
                                       chat_id=obj.owner.tg_chat_id)
                else:
                    user_chat_id = get_chat_id(obj.owner.tg_username, obj.owner.id)
                    message_send.delay(time=obj.time, owner=obj.owner, place=obj.place, action=obj.action,
                                       chat_id=user_chat_id)
        else:
            if obj.time() <= time_now.time():
                obj.last_send = time_now
                obj.save()
                if obj.owner.tg_chat_id:
                    message_send.delay(time=obj.time, owner=obj.owner, place=obj.place, action=obj.action,
                                       chat_id=obj.owner.tg_chat_id)
                else:
                    chat_id = get_chat_id(obj.owner.tg_username, obj.owner.id)
                    message_send.delay(time=obj.time, owner=obj.owner, place=obj.place, action=obj.action,
                                       chat_id=chat_id)
