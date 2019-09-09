import os
from bot import app
from bot import commands
from bot.cron import search, news
from flask import request


@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == 'GET':
        return 'Бот для телеграм чата.'
    elif request.method == 'POST':
        commands.run()

        return 'OK'


@app.route(f"/{os.environ['PATH_CRON_SEARCH']}/", methods=['POST'])
def cron_search():
    if request.method == 'POST':
        search.main()

        return 'OK'


@app.route(f"/{os.environ['PATH_CRON_NEWS']}/", methods=['POST'])
def cron_news():
    if request.method == 'POST':
        news.main()

        return 'OK'