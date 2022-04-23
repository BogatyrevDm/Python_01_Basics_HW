import os

# Создадим список папок.
dirs_list = [r'my_project',
             r'my_project\settings',
             r'my_project\mainapp',
             r'my_project\dminapp',
             r'my_project\authapp']

# Определим базовый путь для сохранения
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Переберем список
for i in dirs_list:
    # Получим полный путь
    full_path = os.path.join(BASE_DIR, i)
    # Проверим папку на существование
    if not os.path.exists(full_path):
        # Создадим папку
        os.mkdir(full_path)
