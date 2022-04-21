import json
import itertools


def prepare_dataset(path_users_file: str, path_hobby_file: str) -> dict:
    """
    Считывает данные из файлов и возвращает словарь, где:
        ключ — ФИО, значение — данные о хобби (список строковых переменных)
    :param path_users_file: путь до файла, содержащий ФИО пользователей, разделенных запятой по строке
    :param path_hobby_file: путь до файла, содержащий хобби, разделенные запятой по строке
    :return: Dict(str: Union[List[str]|None])
    """

    user_list = []
    # Прочитаем список пользователей. Требований по ОЗУ нет, поэтому читаем сразу
    with open(path_users_file, 'r', encoding='utf-8') as users_file:
        user_list = users_file.read().splitlines()

    # Прочитаем список хобби. Требований по ОЗУ нет, поэтому читаем сразу
    hobby_list = []
    with open(path_hobby_file, 'r', encoding='utf-8') as hobbies_file:
        hobby_list = hobbies_file.read().splitlines()

    # Если список пользователей короче - возвращаем 1
    if len(user_list) < len(hobby_list):
        return 1

    # Преобразуем в словарь 2 списка. Возможно, zip_longest - чит, но оставлю:)
    users_dict = {user.replace(',', ' '): hobby for user, hobby in itertools.zip_longest(user_list, hobby_list)}

    return users_dict


dict_out = prepare_dataset('users.csv', 'hobby.csv')
with open('task_6_3_result.json', 'w', encoding='utf-8') as fw:
    json.dump(dict_out, fw, ensure_ascii=False, indent=2)

# попробуем прочитать сохраненный файл
with open('task_6_3_result.json', 'r', encoding='utf-8') as fr:
    result = json.loads(fr.read())
    print(result)
