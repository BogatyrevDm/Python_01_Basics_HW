import os
from collections import defaultdict

# Определим базовый путь для перебора
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

size_dict = defaultdict(tuple)

# Обойдем рекурсивно папку
# Я накидал в папку файликов разных размеров для тестирования. Также в результат попадут сами файлы скриптов
for root, dirs, files in os.walk(BASE_DIR):
    # Переберем файлы в папке
    for file in files:
        # Получим размер
        size = os.stat(os.path.join(root, file)).st_size
        # Определим категорию, в которую попадает файл, возведя 10 в степень длины размера
        size_group = 10 ** (len(str(size)))
        # Получим расширение
        ext = file.rsplit('.', maxsplit=1)[-1]
        # Если кортеж еще пуст - добавим количество и создадим список с расширениями
        if len(size_dict[size_group]) == 0:
            size_dict[size_group] = (1, [ext])
        else:
            # В противном случае - создадим новый кортеж и поместим туда новые значения
            ext_list = size_dict[size_group][1]
            count = ext_list.count(ext) > 0
            if count == 0:
                ext_list.append(ext)
            files_count = size_dict[size_group][0] + 1
            size_dict[size_group] = (files_count, ext_list)

    # Отсортируем словарь по убыванию ключей
    dict_sorted = dict(sorted(size_dict.items(), key=lambda x: len(str(x[0])), reverse=True))

    # Выведем результат
    print(dict_sorted)
