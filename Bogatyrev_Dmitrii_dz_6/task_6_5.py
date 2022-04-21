import itertools


def prepare_dataset(path_users_file: str, path_hobby_file: str, path_result_file: str):
    """
    Считывает данные из файлов и сохраняет в текстовый файл строку вида:
        ФИО : данные о хобби
    :param path_users_file: путь до файла, содержащий ФИО пользователей, разделенных запятой по строке
    :param path_hobby_file: путь до файла, содержащий хобби, разделенные запятой по строке
    :param path_result_file: путь до файла результата
    """

    user_list = []
    # Прочитаем список пользователей. Читаем последовательно, потому что есть требования по ОЗУ
    with open(path_users_file, 'r', encoding='utf-8') as users_file:
        for line in users_file:
            user_list.append(line.strip())

    # Прочитаем список хобби. Читаем последовательно, потому что есть требования по ОЗУ
    hobby_list = []
    with open(path_hobby_file, 'r', encoding='utf-8') as hobbies_file:
        for line in hobbies_file:
            hobby_list.append(line.strip())

    # Если список пользователей короче - возвращаем 1
    if len(user_list) < len(hobby_list):
        return 1

    # Преобразуем 2 cписка в общий список. Возможно, zip_longest - чит, но оставлю:)
    # Символ переноса добавляем ультимативно. В выходном файле будет одна лишняя строка в конце, но это не баг, а фича:)
    result_list = [f'{user.replace(",", " ")} : {hobby}\n' for user, hobby in
                   itertools.zip_longest(user_list, hobby_list)]
    # Записываем результирующий файл.
    with open(path_result_file, 'w', encoding='utf-8') as fw:
        fw.writelines(result_list)


if __name__ == '__main__':
    import sys

    if type(sys.argv) == list and len(sys.argv) > 3:
        program, path_users_file, path_hobby_file, path_result_file = sys.argv
        prepare_dataset(path_users_file, path_hobby_file, path_result_file)
