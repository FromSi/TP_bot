from flask import request


def parse():
    return request.get_json()


def chat():
    return parse()['message']['chat']


def chat_id():
    return parse()['message']['chat']['id']


def type():
    return parse()['message']['chat']['type']


def command():
    if parse()['message'].get('text') is not None:
        return parse()['message']['text']
    return None


def username():
    if parse()['message'].get('from') is not None:
        if parse()['message'].get('from').get('username'):
            return parse()['message']['from']['username']
    return None


def first_name():
    if parse()['message'].get('from') is not None:
        if parse()['message'].get('from').get('first_name'):
            return parse()['message']['from']['first_name']
    return None


def last_name():
    if parse()['message'].get('from') is not None:
        if parse()['message'].get('from').get('last_name'):
            return parse()['message']['from']['last_name']
    return None


def message_id():
    return parse()['message']['message_id']