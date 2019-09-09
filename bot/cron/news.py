from bot import models


def main():
    news = models.News.query.first()

    if news is not None:
        text = '✏️ Новости\n'
        text += f'📝 {news.count} новости(-ей,-ь)!\n'
        text += '📎 https://t.me/illuminatiinc'

        news.count = 0
        db.session.add(news)
        db.session.commit()