from util import horoscope


def get_horoscope(name):
    text = f'{_get_emoji_horoscope(name)} Гороскоп на сегодня:'
    text += f'{horoscope.get_horoscope(name)}'
    
    return text


def _get_emoji_horoscope(name):
    if name == 'aries':
        return '♈️'
    elif name == 'taurus':
        return '♉️'
    elif name == 'gemini':
        return '♊️'
    elif name == 'cancer':
        return '♋️'
    elif name == 'leo':
        return 'leo'
    elif name == 'virgo':
        return '♍️'
    elif name == 'libra':
        return '♎️'
    elif name == 'scorpio':
        return '♏️'
    elif name == 'sagittarius':
        return '♐️'
    elif name == 'capricorn':
        return '♑️'
    elif name == 'aquarius':
        return '♒️'
    elif name == 'pisces':
        return '♓️'