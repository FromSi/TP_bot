from bot.messages import pidor_stat
from bot import models, db


def main(data):
    return _router(data)


def _router(data):
    if data['message']['text'] == '/pidorrate@pidroid65_bot':
        return pidor_stat.get_rate()
    elif data['message']['text'] == '/pidormembers@pidroid65_bot':
        return pidor_stat.get_members()
    elif data['message']['text'] == '/pidorswitch@pidroid65_bot':
        return pidor_stat.get_switch(_handler_pidor_switch(data))


def _handler_pidor_switch(data):
    username = data['message']['from']['username']
    user = models.User.query.filter_by(username=username).first()
    
    if user is None:
        return 3
    else:
        user_id = user.id
        player = models.PidorGame.query.filter_by(user_id=user_id).first()

        if player is None:
            new_player = models.PidorGame(is_active=True, user=user)
            db.session.add(new_player)
            db.session.commit()
            
            return 1
        else:
            player.is_active = not player.is_active
            db.session.add(player)
            db.session.commit()

            if player.is_active:                
                return 1
            else:
                return 2


