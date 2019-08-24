from bot.cron.util import weather


def get_weather(weather_link):
    array = weather.get_weather(weather_link)
    text = '⛅️ Погода на сегодня:\n'
    
    for item in array:
        text += f'{_get_emoji_time(item[0])}  🌡 {item[1]}  🌬 {item[2]}м/c\n'

    return text


def _get_emoji_time(time):
    if time == '6':
        return '🕕 06:00'
    elif time == '9':
        return '🕘 09:00'
    elif time == '12':
        return '🕛 12:00'
    elif time == '15':
        return '🕞 15:00'
    elif time == '18':
        return '🕡 18:00'
    elif time == '21':
        return '🕤 21:00'