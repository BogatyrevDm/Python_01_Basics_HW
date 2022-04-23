import os
from collections import defaultdict

# Определим базовый путь для перебора
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

size_dict = defaultdict(int)

# Обойдем рекурсивно папку
# Я накидал в папку файликов разных размеров для тестирования. Также в результат попадут сами файлы скриптов
for root, dirs, files in os.walk(BASE_DIR):
    # Переберем файлы в папке
    for file in files:
        # Получим размер
        size = os.stat(os.path.join(root, file)).st_size
        # Определим категорию, в которую попадает файл, возведя 10 в степень длины размера
        size_group = 10 ** (len(str(size)))
        # Поместим в соответсвующую группу в словаре
        size_dict[size_group] += 1
    # Отсортируем словарь по убыванию ключей
    dict_sorted = dict(sorted(size_dict.items(), key=lambda x: len(str(x[0])), reverse=True))
    # Выведем результат: {10000: 4, 1000: 3, 100: 2, 10: 2}
    print(dict_sorted)
