"""Генератор приветствий."""


def greetings(name: str) -> str:
    """Возвращает текст приветствия.

    Args:
        name: Имя для приветствия.

    Returns:
        Текст приветствия.

    """
    return 'Привет, {name}'.format(name=name.title())
