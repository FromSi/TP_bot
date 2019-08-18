import os


TOKEN = os.environ['TOKEN_BOT']
URL = f'https://api.telegram.org/bot{TOKEN}/'
CHAT_ID = os.environ['CHAT_ID']


def get_send_message():
    return f'{URL}sendMessage'