from bot.util.telegram import parser, api


def listener_content():
    if parser.text() is not None:
        pass
    elif parser.forward_from_message_id is not None:
        api.forwardMessage(api.CHAT_ID, api.CHAT_NEWS_ID, parser.message_id())
        api.deleteMessage(parser.message_id, api.CHAT_ID)


def listener_news():
    pass