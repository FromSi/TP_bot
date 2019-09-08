from bot import db


class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    count = db.Column(db.Integer)


class Emoji(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(255))


class Horoscope(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    emoji_id = db.Column(
        db.Integer, db.ForeignKey('emoji.id'),
        nullable=False
    )
    emoji = db.relationship(
        'Emoji',
        backref=db.backref('horoscope', lazy=True)
    )


class Weather(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    link = db.Column(db.String(255))


class StatPidor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    count = db.Column(db.Integer)
    
    user_id = db.Column(
        db.Integer, db.ForeignKey('user.id'),
        nullable=False
    )
    user = db.relationship(
        'User',
        backref=db.backref('stat_pidors', lazy=True)
    )


class PidorGame(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    is_active = db.Column(db.Boolean)

    user_id = db.Column(
        db.Integer, db.ForeignKey('user.id'),
        nullable=False
    )
    user = db.relationship(
        'User',
        backref=db.backref('pidor_games', lazy=True)
    )


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    weather_id = db.Column(
        db.Integer, db.ForeignKey('weather.id'),
        nullable=False
    )
    weather = db.relationship(
        'Weather',
        backref=db.backref('user', lazy=True)
    )
    horoscope_id = db.Column(
        db.Integer, db.ForeignKey('horoscope.id'),
        nullable=False
    )
    horoscope = db.relationship(
        'Horoscope',
        backref=db.backref('user', lazy=True)
    )