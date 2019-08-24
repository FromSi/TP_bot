import os
from bot import app
from bot import commands
from bot.cron import search
from bot.util import http_methods


@app.route("/", methods=["GET", "POST"])
def main():
    return http_methods.base(
        get='Бот для телеграм чата.',
        post=commands.run()
    )


@app.route(f"/{os.environ['PATH_CRON_SEARCH']}/", methods=['POST'])
def cron_search():
    return http_methods.base(
        post=search.main()
    )