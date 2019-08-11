import os


TOKEN = os.environ['TOKEN_BOT']
URL = f'https://api.telegram.org/bot{TOKEN}/'


def get_send_message():
    return f'{URL}sendMessage'