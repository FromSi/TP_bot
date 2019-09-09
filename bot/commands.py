from bot.messages import pidor_stat
from bot.util.telegram import parser, api
from bot import models, db
from bot import news as news_handler
from bot.messages import horoscope, weather, news, start, help
from bot.util import helpers, auth


def run():
    return _router()


def _router():
    # print('INFO:', parser.parse())

    news_handler.run()

    if parser.text() is not None:
        command = parser.text()
        message_id = parser.message_id()
        chat_id = parser.chat_id()
        chat_type = parser.type()

        if command == '/start':
            if auth.is_private(chat_type):
                api.sendMarkdownMessage(
                    chat_id,
                    start.data()
                )

        elif command == '/help':
            if parser.username() is not None:
                if auth.is_private_auth(chat_type, parser.username()):
                    api.sendMarkdownMessage(
                        chat_id,
                        help.data()
                    )
            else:
                return 'ERR'

        elif command == '/pidorrate@pidroid65_bot' or command == '/pidorrate':
            if auth.is_private_or_supergroup(chat_type, chat_id):
                api.sendMessage(
                    chat_id,
                    pidor_stat.get_rate()
                )

        elif command == '/pidormembers@pidroid65_bot' or command == '/pidormembers':
            if auth.is_private_or_supergroup(chat_type, chat_id):
                api.sendMessage(
                    chat_id,
                    pidor_stat.get_members()
                )

        elif command == '/pidorswitch@pidroid65_bot' or command == '/pidorswitch':
            if auth.is_private_or_supergroup(chat_type, chat_id):
                api.sendMessage(
                    chat_id,
                    _pidor_switch()
                )

        elif command == '/weather@pidroid65_bot' or command == '/weather':
            if auth.is_private_or_supergroup(chat_type, chat_id):
                api.sendReplyMessage(
                    message_id, 
                    chat_id,
                    _weather()
                )

        elif command == '/horoscope@pidroid65_bot' or command == '/horoscope':
            if auth.is_private_or_supergroup(chat_type, chat_id):
                api.sendReplyMessage(
                    message_id, 
                    chat_id,
                    _horoscope()
                )

        elif command[0:len('/s')] == '/s':
            if command[0:len('/sa')] == '/sa':
                if parser.username() is not None and parser.first_name() is not None:
                    if auth.is_private_or_supergroup_auth(chat_type, chat_id, parser.username()):
                        text = news.sa(parser.first_name(), command[len('/sa') + 1:])

                        api.sendMarkdownMessage(
                            api.CHAT_ID,
                            text
                        )
                        api.sendMarkdownMessage(
                            api.CHAT_NEWS_ID,
                            text
                        )
                        api.deleteMessage(
                            message_id,
                            chat_id
                        )

                        news_handler.add_news()

            elif parser.username() is not None and parser.first_name() is not None:
                if auth.is_private_or_supergroup_auth(chat_type, chat_id, parser.username()):
                    text = news.s(parser.first_name(), command[len('/s') + 1:])
                    
                    api.sendMarkdownMessage(
                        api.CHAT_ID,
                        text
                    )
                    api.sendMarkdownMessage(
                        api.CHAT_NEWS_ID,
                        text
                    )
                    api.deleteMessage(
                        message_id,
                        chat_id
                    )

                    news_handler.add_news()
            else: 
                return 'ERR'

        elif command[0:len('/w')] == '/w':
            if command[0:len('/wa')] == '/wa':
                if parser.username() is not None and parser.first_name() is not None:
                    if auth.is_private_or_supergroup_auth(chat_type, chat_id, parser.username()):
                        api.sendMarkdownMessage(
                            api.CHAT_ID,
                            news.wa(parser.first_name(), command[len('/wa') + 1:])
                        )
                        api.deleteMessage(
                            message_id,
                            chat_id
                        )
            elif parser.username() is not None and parser.first_name() is not None:
                if auth.is_private_or_supergroup_auth(chat_type, chat_id, parser.username()):
                    api.sendMarkdownMessage(
                        api.CHAT_ID,
                        news.w(parser.first_name(), command[len('/w') + 1:])
                    )
                    api.deleteMessage(
                        message_id,
                        chat_id
                    )
            else: 
                return 'ERR'
    else:
        return 'ERR'


def _weather():
    if parser.username() is not None:
        username = parser.username()
        user = models.User.query.filter_by(username=username).first()

        if user is None:
            return 'Ты вначале зарегайся, а потом проси..'
        else:
            obj = helpers.weather(user)

            return weather.data(obj['link'])
    else:
        return 'ERR'


def _horoscope():
    if parser.username() is not None:
        username = parser.username()
        user = models.User.query.filter_by(username=username).first()

        if user is None:
            return 'Ты вначале зарегайся, а потом проси..'
        else:
            obj = helpers.horoscope(user)

            return horoscope.data(obj['name'], obj['symbol'])
    else:
        return 'ERR'


def _pidor_switch():
    if parser.username() is not None:
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
    else:
        return 'ERR'