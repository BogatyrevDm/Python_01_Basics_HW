from pprint import pprint


def get_parse_attrs(line: str) -> tuple:
    # разделяем по пробелам
    line_listed = line.split()
    # берем нужные нам позиции списка
    return line_listed[0], line_listed[5].replace('"', ""), line_listed[6]


list_out = list()
with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:
    # указаний по поводу объема ОЗУ нет, будем считать, что объем ОЗУ больше файла
    # читаем его сразу и преобразуем в список без символов переноса строк
    content_list = fr.read().splitlines()
    # перебираем список и парсим кажду строку
    for line in content_list:
        parsed_tuple = get_parse_attrs(line)
        list_out.append(parsed_tuple)
pprint(list_out)
