import os

import requests

from users.models import User

TOKEN = os.getenv('TG_BOT_TOKEN')
URL = f"https://api.telegram.org/bot{TOKEN}"


def message_send(owner, place, action, time, chat_id):
    param = {
        "chat_id": chat_id,
        "text": f'{owner}, you must do {action} in {place} at {time}'
    }
    response = requests.get(f'{URL}/sendMessage', params=param)



def get_chat_id(username, user_id):
    response = requests.get(f'{URL}/getUpdates')
    for result in response.json().get('result'):
        if result['message']['from']['username'] == username:
            user = User.objects.get(user_id)
            user.tg_chat_id = result['message']['chat']['id']
            user.save()
            return result['message']['chat']['id']
