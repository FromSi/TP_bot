import re
from bot.util.telegram import parser, api
from bot import models, db


def run():
    _listener_content()
    _listener_news()


def _listener_content():
    if str(api.CHAT_ID) == str(parser.chat_id()):

        if parser.forward_from is not None:
            print(1)
            _send_message()
            _add_count_news()
        elif parser.text() is not None:
            print(2)
            if _check_links():
                print(3)
                _send_message()
                _add_count_news()

    
def _listener_news():
    if str(api.CHAT_NEWS_ID) == str(parser.channel_id()):
        print(4)
        _add_count_news()


def _add_count_news():
    news = models.News.query.first()

    if news is not None:
        news.count += 1
        db.session.add(news)
        db.session.commit()
    else:
        new_news = models.News(count=1)
        db.session.add(new_news)
        db.session.commit()
    
    print(news.count)


def _check_links():
    links = re.findall(
            'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
             parser.text()
        )
    return len(links) != 0


def _send_message():
    api.forwardMessage(api.CHAT_NEWS_ID, api.CHAT_ID, parser.message_id())
    api.deleteMessage(parser.message_id, api.CHAT_ID)