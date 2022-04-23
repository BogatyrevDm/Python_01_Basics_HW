import os


# Сделаю отдельной функцией, что бы использовать в третьем задании
def create_file_structure_by_template():
    # Определим базовый путь для сохранения
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    # Сделаю проверку на глобальную ошибку, ничего специфичного придумать не смог
    try:
        # Откроем файл на чтение
        with open('config.yaml', 'r', encoding='utf-8') as fr:
            content = fr.readlines()
            # Переберем список
            for i in content:
                # Получим полный путь
                full_path = os.path.join(BASE_DIR, i.strip())
                # Проверим папку на существование
                if not os.path.exists(full_path):
                    # Если в пути есть точка - это файл
                    if i.find('.') > 0:
                        # Создадим файл
                        file = open(full_path, 'w', encoding='utf-8')
                        file.close()
                    else:
                        # Создадим папку
                        os.mkdir(full_path)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    create_file_structure_by_template()
