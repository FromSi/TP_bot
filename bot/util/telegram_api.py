import os, requests
from bot.util import telegram_parse
from bot import commands


TOKEN = os.environ['TOKEN_BOT']
CHAT_ID = os.environ['CHAT_ID']
URL = f'https://api.telegram.org/bot{TOKEN}/'


def sendMessage():
    requests.post(
        _url_send_message(),
        data={
            'chat_id': CHAT_ID, 
            'text': commands.main(telegram_parse.parse()), 
            'disable_notification': True
        }
    )


def _url_send_message():
    return f'{URL}sendMessage'