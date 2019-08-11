from bot import models, db


def get_members():
    text = 'Список пидорасов\n\n'
    members_on = models.PidorGame.query.filter_by(is_active=True)
    members_off = models.PidorGame.query.filter_by(is_active=False)

    if members_on.first() is not None:
        text += 'Играют:\n'
        text += _get_members(members_on)
        text += '\n\n'
    elif members_off.first() is not None:
        text += 'Не играют:\n'
        text += _get_members(members_off)
        text += '\n\n'

    text += 'Расчёт пидорасов окончен!'

    return text


def get_rate():
    text = 'Рейтинг пидорасов:\n'
    members = models.StatPidor.query
    
    if members.first() is not None:
        text += _get_rate(members)
        text += '\n\n'

    return text


def get_switch(code):
    if code == 1:
        return 'Всё! Ты в игре!! ТОБИ ПЕЗТА!!!'
    elif code == 2:
        return 'С тобой ВСЁ!'
    elif code == 3:
        return 'Тебя еще не зарегали в базу пользователей! Ты нахуй никому не нужен!'


def _get_members(members):
    text = ''

    for i in range(members.count()):
        user = models.User.query.get(members.all()[i].user_id)
        text += f'\t\t{i + 1}) @{user.username}'

    return text


def _get_rate(members):
    text = ''

    for i in range(members.count()):
        user = models.User.query.get(members.all()[i].user_id)
        text += f'\t\t@{user.username} - {members.all()[i].count} раз(а)'

    return text

