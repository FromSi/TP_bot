import re
from bot.util.telegram import parser, api


def listener_content():
    if parser.text() is not None:
        if _check_links():
            _send_message()
    elif parser.forward_from_message_id is not None:
        _send_message()


def listener_news():
    pass


def _check_links():
    links = re.findall(
            'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
             parser.text()
        )
    return len(links) != 0


def _send_message():
    api.forwardMessage(api.CHAT_NEWS_ID, api.CHAT_ID, parser.message_id())
    api.deleteMessage(parser.message_id, api.CHAT_ID)