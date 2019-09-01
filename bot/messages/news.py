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
    'ЕБАААААтть читать всем!',
    'Вы щас уйдёте в унисон!',
    'Контент подвезли!',
    'От такой новости Ленин перевернулся!',
    'Слабонерным лучше этого не видеть!',
]


def data(first_name, last_name, body):
    text = _title()
    text += '\n\n'
    text += body
    text += '\n\n'
    text += f'_Автор: {first_name} {last_name}_'

    return text


def _title():
    title = ''

    for i in range(3):
        title += emoji_list[randrange(len(emoji_list))]

    title += '*' + title_list[randrange(len(title_list))].upper() + '*'

    for i in range(3):
        title += emoji_list[randrange(len(emoji_list))]

    return title