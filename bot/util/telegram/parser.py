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
    return parse()['message']['text']


def username():
    return parse()['message']['from']['username']


def first_name():
    return parse()['message']['from']['first_name']


def last_name():
    return parse()['message']['from']['last_name']


def message_id():
    return parse()['message']['message_id']