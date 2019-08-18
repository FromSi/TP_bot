from bot import app
from bot import models
from flask import request
from bot.util import telegram_api
from bot import commands
import requests, os
from bot.cron import search


@app.route("/", methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        data = request.get_json()
        chat_id = data['message']['chat']['id']

        requests.post(
            telegram_api.get_send_message(),
            data={
                'chat_id': telegram_api.CHAT_ID, 
                'text': commands.main(data), 
                'disable_notification': True
            }
        )

        return 'OK'
    elif request.method == 'GET':
        return 'I bot'


@app.route(f"/{os.environ['PATH_CRON_SEARCH']}/", methods=['POST'])
def cron_search():
    if request.method == 'POST':
        search.main()

        return 'OK'