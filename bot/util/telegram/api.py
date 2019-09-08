import os, requests
from bot import commands


TOKEN = os.environ['TOKEN_BOT']
CHAT_ID = os.environ['CHAT_ID']
CHAT_NEWS_ID = os.environ['CHAT_NEWS_ID']
URL = f'https://api.telegram.org/bot{TOKEN}/'


def sendMessage(chat_id, text):
    requests.post(
        _url_send_message(),
        data={
            'chat_id': chat_id, 
            'text': text, 
            'disable_notification': True
        }
    )


def sendMarkdownMessage(chat_id, text):
    requests.post(
        _url_send_message(),
        data={
            'chat_id': chat_id, 
            'text': text, 
            'parse_mode': 'Markdown',
            'disable_notification': True
        }
    )

def sendReplyMessage(message_id, chat_id, text):
    requests.post(
        _url_send_message(),
        data={
            'chat_id': chat_id, 
            'text': text, 
            'reply_to_message_id': message_id,
            'disable_notification': True
        }
    )

def forwardMessage(chat_id, from_chat_id, message_id):
    requests.post(
        _url_forward_message(),
        data={
            'chat_id': chat_id, 
            'from_chat_id': from_chat_id, 
            'message_id': message_id,
            'disable_notification': True
        }
    )

def deleteMessage(message_id, chat_id):
    requests.post(
        _url_delete_message(),
        data={
            'chat_id': chat_id, 
            'message_id': message_id, 
        }
    )


def _url_send_message():
    return f'{URL}sendMessage'


def _url_delete_message():
    return f'{URL}deleteMessage'


def _url_forward_message():
    return f'{URL}forwardMessage'