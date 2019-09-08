from flask import request


def parse():
    return request.get_json()


def message():
    if parse().get('message') is not None:
        return parse().get('message')
    return None


def chat():
    if message():
        return parse()['message']['chat']
    return None


def chat_id():
    if chat() is not None:
        return parse()['message']['chat']['id']
    return None


def channel_id():
    if parse().get('channel_post') is not None:
        return parse().get('channel_post')['chat']['id']
    return None


def type():
    if chat() is not None:
        return parse()['message']['chat']['type']
    return None


def text():
    if message():
        if message().get('text') is not None:
            return message().get('text')
    return None


def username():
    if message().get('from') is not None:
        if message().get('from').get('username'):
            return message().get('from').get('username')
    return None


def first_name():
    if message().get('from') is not None:
        if message().get('from').get('first_name'):
            return message().get('from').get('first_name')
    return None


def last_name():
    if message().get('from') is not None:
        if message().get('from').get('last_name'):
            return message().get('from').get('last_name')
    return None


def message_id():
    if message():
        return message()['message_id']
    return None


def forward_from_message_id():
    if message() and message().get('forward_from_message_id') is not None:
        return message().get('forward_from_message_id')
    return None