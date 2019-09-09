import sqlalchemy as db
import random, os, requests
from bot.messages import weather, horoscope
from bot.util.telegram import api
from sqlalchemy import update
from bot.util import helpers


engine = db.create_engine(os.environ['DATABASE_URL'])
connection = engine.connect()
metadata = db.MetaData()

from bot import news


def main():
    players = _get_players_pidor_game()

    if len(players) != 0:
        user = _get_user(random.choice(players).user_id)
        obj_weather = helpers.weather(user)
        obj_horoscope = helpers.horoscope(user)

        text = f'Сегодня пидор @{user.username}!\n\n'
        text += horoscope.data(obj_horoscope['name'], obj_horoscope['symbol'])
        text += '\n' + weather.data(obj_weather['link'])

        api.sendMessage(api.CHAT_ID, text + '\n🤖 Бета версия')
        _write_result(user)

        news.add_news()
        api.sendMessage(api.CHAT_NEWS_ID, text)


def _write_result(user):
    stat_pidor = db.Table('stat_pidor', metadata, autoload=True, autoload_with=engine)
    stat_pidor_query = db.select([stat_pidor]).where(stat_pidor.columns.user_id == user.id)
    result_proxy = connection.execute(stat_pidor_query)
    players = result_proxy.fetchall()

    if len(players) == 0:
        query = db.insert(stat_pidor)
        value = {
            'user_id': user.id,
            'count': 1
            }
        connection.execute(query, value)
    else:
        query = update(
            stat_pidor
        ).where(
            stat_pidor.columns.user_id == user.id
        ).values(
            count=(players[0].count + 1)
        )
        connection.execute(query)


def _get_players_pidor_game():
    pidor_game = db.Table('pidor_game', metadata, autoload=True, autoload_with=engine)
    pidor_game_query = db.select([pidor_game]).where(pidor_game.columns.is_active == True)
    result_proxy = connection.execute(pidor_game_query)

    return result_proxy.fetchall()


def _get_user(id):
    user = db.Table('user', metadata, autoload=True, autoload_with=engine)
    user_query = db.select([user]).where(user.columns.id == id)
    result_proxy = connection.execute(user_query)

    return result_proxy.fetchall()[0]
