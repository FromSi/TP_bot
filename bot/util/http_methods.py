from flask import request


def base(get=None, post=None, delete=None, put=None):
    if request.method == 'GET':
        get()

        return 'OK'
    elif request.method == 'POST':
        post()

        return 'OK'
    elif request.method == 'DELETE':
        delete()

        return 'OK'
    elif request.method == 'PUT':
        put()

        return 'OK'