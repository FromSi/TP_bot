from flask import request


def parse():
    return request.get_json()


def chat():
    return parse()['message']['chat']