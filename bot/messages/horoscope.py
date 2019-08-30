from bot.util import horoscope


def data(name, symbol):
    text = f'{symbol} Гороскоп на сегодня:'
    text += f'{horoscope.data(name)}'
    
    return text