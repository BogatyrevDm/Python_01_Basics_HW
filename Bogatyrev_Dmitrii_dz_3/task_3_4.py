def thesaurus_adv(*args) -> dict:
    '''Функция преобразует переданные аргументы в словарь'''
    dict_out = {}  # результирующий словарь значений

    # Переберем переданный кортеж
    for i in args:
        # Определим первый символ фамилии
        first_simbol = i.split(" ")[1][0]
        # Если первый символ фамилии есть в словаре - получим его,
        # иначе добавим в словарь с пустым словарем
        names_dict = dict_out.setdefault(first_simbol, {})
        # Определим первый символ имени
        name_first_simbol = i[0]
        # Если первый символ имени есть в словаре - получим его,
        # иначе добавим в словарь с пустым списком
        names_list = names_dict.setdefault(name_first_simbol, [])
        # Добавим в список имен имя.
        # Повторяющиеся имена будут добавлены несколько раз.
        # Но в условии это отдельно не оговорено
        names_list.append(i)
    return dict_out


def sort_dict(dict_in: dict) -> dict:
    '''Функция сортирует словарь, который получет на вход'''
    # Способ не самый оптимальный, приходится создавать новый словарь
    # Получаем список ключей и сортируем его
    thesaurus_list = list(thesaurus_dict)
    thesaurus_list.sort()
    dict_out = {}
    # Перебираем отсортированный список
    for i in thesaurus_list:
        # Получаем по ключу значения из исходного словаря
        # и добавлем их в новый словарь
        dict_out[i] = dict_in.get(i)
    return dict_out


thesaurus_dict = thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
print(thesaurus_dict)

thesaurus_dict_sorted = sort_dict(thesaurus_dict)
print(thesaurus_dict_sorted)
