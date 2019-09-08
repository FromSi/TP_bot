from bot.util.telegram import parser, api


def listener_content():
    if parser.text() is not None:
        print(1231312313123123123123213131231312321312321311)
    elif parser.forward_from_message_id is not None:
        api.forwardMessage(api.CHAT_ID, api.CHAT_NEWS_ID, parser.message_id())
        api.deleteMessage(parser.message_id, api.CHAT_ID)


def listener_news():
    pass