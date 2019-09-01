from bot.messages import pidor_stat
from bot.util.telegram import parser, api
from bot import models, db
from bot.messages import horoscope, weather, news, start, help
from bot.util import helpers, auth


def run():
    return _router()


def _router():
    command = parser.command()
    message_id = parser.message_id()
    chat_id = parser.chat_id()
    chat_type = parser.type()
    username = parser.username()
    first_name = parser.first_name()

    if command == '/start':
        if auth.is_private(chat_type):
            api.sendMarkdownMessage(
                chat_id,
                start.data()
            )

    elif command == '/help':
        if auth.is_private_auth(chat_type, username):
            api.sendMarkdownMessage(
                chat_id,
                help.data()
            )

    elif command == '/pidorrate@pidroid65_bot':
        if auth.is_private_or_supergroup(chat_type, chat_id):
            api.sendMessage(
                chat_id,
                pidor_stat.get_rate()
            )

    elif command == '/pidormembers@pidroid65_bot':
        if auth.is_private_or_supergroup(chat_type, chat_id):
            api.sendMessage(
                chat_id,
                pidor_stat.get_members()
            )

    elif command == '/pidorswitch@pidroid65_bot':
        if auth.is_private_or_supergroup(chat_type, chat_id):
            api.sendMessage(
                chat_id,
                _pidor_switch()
            )

    elif command == '/weather@pidroid65_bot':
        if auth.is_private_or_supergroup(chat_type, chat_id):
            api.sendReplyMessage(
                message_id, 
                chat_id,
                _weather()
            )

    elif command == '/horoscope@pidroid65_bot':
        if auth.is_private_or_supergroup(chat_type, chat_id):
            api.sendReplyMessage(
                message_id, 
                chat_id,
                _horoscope()
            )

    elif command[0:len('/w')] == '/w':
        if auth.is_private_or_supergroup_auth(chat_type, chat_id, username):
            api.sendMarkdownMessage(
                api.CHAT_ID,
                news.data(first_name, last_name, command[len('/w') + 1:])
            )
            api.deleteMessage(
                message_id,
                chat_id
            )


def _weather():
    username = parser.username()
    user = models.User.query.filter_by(username=username).first()

    if user is None:
        return 'Ты вначале зарегайся, а потом проси..'
    else:
        obj = helpers.weather(user)

        return weather.data(obj['link'])


def _horoscope():
    username = parser.username()
    user = models.User.query.filter_by(username=username).first()

    if user is None:
        return 'Ты вначале зарегайся, а потом проси..'
    else:
        obj = helpers.horoscope(user)
        
        return horoscope.data(obj['name'], obj['symbol'])


def _pidor_switch():
    username = parser.username()
    user = models.User.query.filter_by(username=username).first()
    
    answer_one = 'Тебя еще не зарегали в базу пользователей! Ты нахуй никому не нужен!'
    answer_two = 'Всё! Ты в игре!! ТОБИ ПЕЗТА!!!'
    answer_three = 'С тобой ВСЁ!'

    if user is None:
        return answer_one
    else:
        user_id = user.id
        player = models.PidorGame.query.filter_by(user_id=user_id).first()

        if player is None:
            new_player = models.PidorGame(is_active=True, user=user)
            db.session.add(new_player)
            db.session.commit()
            
            return answer_two
        else:
            player.is_active = not player.is_active
            db.session.add(player)
            db.session.commit()

            if player.is_active:                
                return answer_two
            else:
                return answer_three