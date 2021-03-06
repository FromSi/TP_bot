from bot import models, db


def get_members():
    text = 'Список пидорасов\n\n'
    members_on = models.PidorGame.query.filter_by(is_active=True)
    members_off = models.PidorGame.query.filter_by(is_active=False)

    if members_on.first() is not None:
        text += 'Играют:\n'
        text += _get_members(members_on)
        text += '\n'
    elif members_off.first() is not None:
        text += 'Не играют:\n'
        text += _get_members(members_off)
        text += '\n'

    text += 'Расчёт пидорасов окончен!'

    return text


def get_rate():
    text = 'Рейтинг пидорасов:\n'
    members = models.StatPidor.query
    
    if members.first() is not None:
        text += _get_rate(members)
        text += '\n\n'

    return text


def _get_members(members):
    text = ''

    for i in range(members.count()):
        user = models.User.query.get(members.all()[i].user_id)
        text += f'  {i + 1}) @{user.username}\n'

    return text


def _get_rate(members):
    sort_members = members.order_by(models.StatPidor.count.desc()).all()
    text = ''

    for item in sort_members:
        user = models.User.query.get(item.user_id)
        text += f'  @{user.username} - {item.count} раз(а)\n'

    return text

