from bot import app
from bot import models
from flask import request
from bot.util import telegram_api
from bot import commands
import requests, os
from bot.cron import search
from bot.util import http_methods


@app.route("/", methods=["GET", "POST"])
def telegram():
    return http_methods.base(
        get='Бот для телеграм чата.',
        post=telegram_api.sendMessage()
    )


@app.route(f"/{os.environ['PATH_CRON_SEARCH']}/", methods=['POST'])
def cron_search():
    return http_methods.base(
        request, 
        post=search.main()
    )