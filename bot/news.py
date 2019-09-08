import re
from bot.util.telegram import parser, api
from bot import models, db


def run():
    _listener_content()
    _listener_news()


def _listener_content():
    if parser.text() is not None:
        if _check_links():
            _send_message()
    elif parser.forward_from_message_id is not None:
        _send_message()

    
def _listener_news():
    news = models.News.query.first()

    if news is not None:
        print('news', news.count)
        news.count += 1
        db.session.add(news)
        db.session.commit()
    else:
        new_news = models.News(count=0)
        db.session.add(new_news)
        db.session.commit()


def _check_links():
    links = re.findall(
            'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
             parser.text()
        )
    return len(links) != 0


def _send_message():
    api.forwardMessage(api.CHAT_NEWS_ID, api.CHAT_ID, parser.message_id())
    api.deleteMessage(parser.message_id, api.CHAT_ID)