import os, requests
from bot import commands


TOKEN = os.environ['TOKEN_BOT']
CHAT_ID = os.environ['CHAT_ID']
URL = f'https://api.telegram.org/bot{TOKEN}/'


def sendMessage(text):
    requests.post(
        _url_send_message(),
        data={
            'chat_id': CHAT_ID, 
            'text': text, 
            'disable_notification': True
        }
    )


def sendMarkdownMessage(text):
    requests.post(
        _url_send_message(),
        data={
            'chat_id': CHAT_ID, 
            'text': text, 
            'parse_mode': 'Markdown',
            'disable_notification': True
        }
    )

def sendReplyMessage(message_id, text):
    requests.post(
        _url_send_message(),
        data={
            'chat_id': CHAT_ID, 
            'text': text, 
            'reply_to_message_id': message_id,
            'disable_notification': True
        }
    )

def deleteMessage(message_id):
    requests.post(
        _url_delete_message(),
        data={
            'chat_id': CHAT_ID, 
            'message_id': message_id, 
        }
    )


def _url_send_message():
    return f'{URL}sendMessage'


def _url_delete_message():
    return f'{URL}deleteMessage'