from bot import db


class StatPidor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    count = db.Column(db.Integer)
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),
        nullable=False)
    user = db.relationship('User',
        backref=db.backref('stat_pidors', lazy=True))


class PidorGame(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    is_active = db.Column(db.Boolean)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),
        nullable=False)
    user = db.relationship('User',
        backref=db.backref('pidor_games', lazy=True))


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    weather_city = db.Column(db.String(255), nullable=False)
    horoscope = db.Column(db.String(255), nullable=False)
    username = db.Column(db.String(255), nullable=False)