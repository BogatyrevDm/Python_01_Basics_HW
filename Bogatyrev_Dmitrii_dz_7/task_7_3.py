import os
import shutil

# Определим базовый путь для сохранения
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SRC_NAME = 'my_project'
# Путь к папке my_project
src_dir_path = os.path.join(BASE_DIR, SRC_NAME)

# Если папка не существует - запустим скрипт по созданию из шаблона
if not os.path.exists(src_dir_path):
    from task_7_2 import create_file_structure_by_template

    create_file_structure_by_template()

DEST_NAME = 'templates'
# Путь к папке templates
dest_dir_path = os.path.join(BASE_DIR, DEST_NAME)

# Если папка не существует - запустим скрипт по созданию из шаблона
if not os.path.exists(dest_dir_path):
    os.mkdir(dest_dir_path)

# Сделаю проверку на глобальную ошибку, ничего специфичного придумать не смог
try:
    # Обойдем рекурсивно папку
    for root, dirs, files in os.walk(src_dir_path):
        # Получим имя текущей папки
        base_name = os.path.basename(root)
        # Если имя совпадает с "project", пропустим
        if base_name == SRC_NAME:
            continue
        # Поменяем имя папки в пути на "templates"
        dest_path = root.replace(SRC_NAME, DEST_NAME)
        # Проверим папку на существование
        if not os.path.exists(dest_path):
            # Создадим папку
            os.mkdir(dest_path)
        # Переберем файлы в папке
        for file in files:
            # Получим полные пути - исходный и конечный
            src_file_path = os.path.join(root, file)
            dest_file_path = os.path.join(dest_path, file)
            # Проверим файл на существование
            if not os.path.exists(dest_file_path):
                # Скопируем файл
                shutil.copy2(src_file_path, dest_file_path)
except Exception as e:
    print(e)
