from flask import request


def parse():
    return request.get_json()


def chat():
    return parse()['message']['chat']


def command():
    return parse()['message']['text']


def username():
    return parse()['message']['from']['username']


def message_id():
    return parse()['message']['message_id']