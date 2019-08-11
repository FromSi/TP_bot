TOKEN = 'TOKEN'
URL = f'https://api.telegram.org/bot{TOKEN}/'


def get_send_message():
    return f'{URL}sendMessage'