from random import randrange


emoji_list = [
    '😋','😛','😝','😜','😎',
    '😱','😰','😨','😥','😵',
    '😮','👻','😹','🙀','🗣',
    '🌪','🌈','🔥','💫','⭐',
    '🌊','🍺','☕','🍻','🎰',
    '⏰','☎','🎉','🎊','🖇','🆕',
    '🔖','📈','📉','📯','📮',
    '📦','🆘','💮','❌','⭕',
    '️⛔','️❗','️❕','‼','🆙','🗨',
    '🔈','🔔','📣','🔊','🔉','📢',
    '💬','💭','🗯'
]

title_list = [
    'Всем МОЛЧАТЬ! Новость пришла..',
    'Н-н-новость!!',
    'Шокирующий контекнт!!!',
    'Смотреть всЕм!',
    'Топ контент!!',
    'Сенсация!',
    'Не пропусти СЕКС новость!',
    'Очень важное сообщение!',
    'БЛЯЯ если ты это пропустишь!',
    'Вы щас уйдёте в унисон!',
    'Контент подвезли!',
    'От такой новости Ленин перевернулся!',
    'Слабонерным лучше этого не видеть!',
]


def s(name, body):
    text = _title()
    text += '\n\n'
    text += body
    text += '\n\n'
    text += f'_Автор: {name}_'

    print('s', text)

    return text


def w(name, body):
    text = '*Есть новость..*'
    text += '\n\n'
    text += body
    text += '\n\n'
    text += f'_Автор: {name}_'

    print('w', text)

    return text


def sa(name, body):
    text = _title()
    text += '\n\n'
    text += body

    print('sa', text)

    return text


def wa(name, body):
    text = '*Есть новость..*'
    text += '\n\n'
    text += body

    print('wa', text)

    return text


def _title():
    title = ''

    for i in range(3):
        title += emoji_list[randrange(len(emoji_list))]

    title += '*' + title_list[randrange(len(title_list))].upper() + '*'

    for i in range(3):
        title += emoji_list[randrange(len(emoji_list))]

    return title