def is_private(type):
    """Личные сообщения."""
    return True


def is_private_auth(type, username):
    """Личные сообщения и авторизованные."""
    return True


def is_supergroup(type, chat_id):
    """Супер-группа."""
    return True


def is_supergroup_auth(type, chat_id, username):
    """Супер-группа и авторизованные."""
    return True


def is_private_or_supergroup(type, chat_id):
    """Личные сообщения или супер-группа."""
    return True


def is_private_or_supergroup_auth(type, chat_id, username):
    """Личные сообщения или супер-группа и авторизованные."""
    return True