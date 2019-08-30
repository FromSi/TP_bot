from bot import db, models


def horoscope(user):
    horoscope_model = models.Horoscope.query.filter_by(id=user.horoscope_id).first()
    horoscope_emoji = models.Emoji.query.filter_by(id=horoscope_model.emoji_id).first()

    return {'name': horoscope_model.name, 'symbol': horoscope_emoji.symbol}


def weather(user):
    weather_model = models.Weather.query.filter_by(id=user.weather_id).first()

    return {'link': weather_model.link}