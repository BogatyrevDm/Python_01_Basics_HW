from random import choice, randrange

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

# Соберем все списки в один
all_lists = [nouns, adverbs, adjectives]


def get_jokes(count: int) -> list:
    """Возвращает список шуток в количестве count"""
    list_out = []
    for i in range(count + 1):
        # Получим кортеж из произвольных элементов списка
        words = map(choice, all_lists)
        # Соединим элементы кортежа и поместим в список
        list_out.append(" ".join(words))
    return list_out


print(get_jokes(2))
print(get_jokes(10))


def get_jokes_adv(count: int, allow_repeat: bool = True) -> list:
    """Возвращает список шуток в количестве count"""

    list_out = []
    # Если запрещен повтор слов в шутках, ограничим количество проходов количеством слов в списках
    if not allow_repeat:
        count = min(count, len(nouns) - 1)

    for i in range(count + 1):
        # Получим кортеж из произвольных элементов списка
        if allow_repeat:
            words = map(choice, all_lists)
        else:
            # При получении будем удалять элемент из списка
            words = map(lambda list_in: list_in.pop(randrange(len(list_in))), all_lists)

        # Соединим элементы кортежа и поместим в список
        list_out.append(" ".join(words))
    return list_out

print(get_jokes_adv(2, allow_repeat=False))
print(get_jokes_adv(10, allow_repeat=False))
