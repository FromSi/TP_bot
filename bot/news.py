import re
from bot.util.telegram import parser, api


def listener_content():
    if parser.text() is not None:
        links = re.findall(
            'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
             parser.text()
        )

        if len(links) != 0:
            _send_message()
    elif parser.forward_from_message_id is not None:
        _send_message()
    print(parser.text() is not None, parser.forward_from_message_id is not None)


def listener_news():
    pass


def _send_message():
    api.forwardMessage(api.CHAT_NEWS_ID, api.CHAT_ID, parser.message_id())
    api.deleteMessage(parser.message_id, api.CHAT_ID)