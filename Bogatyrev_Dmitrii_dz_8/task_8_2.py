import re

# Регулярное выражения для парсинга
RE_PARSED_LINE = re.compile(r'([\w.:]*)[\s-]*\[([\S]*\s[+0]*)\]\s"(\w*)\s([\S]*)[^"]*"\s(\d*)\s(\d*)')


def get_parse_attrs(line: str):
    # если строка не попадает в шаблон, выведем сообщение
    if not RE_PARSED_LINE.match(line):
        print(f'Line {line} is not propaly formated')
    # парсим строку
    return RE_PARSED_LINE.findall(line)


with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:
    # Читаем файл сразу и преобразуем в список без символов переноса строк
    content_list = fr.read().splitlines()

    with open('nginx_logs_parsed.txt', 'w', encoding='utf-8') as fw:
        # перебираем список и парсим каждую строку
        for line in content_list:
            parsed_tuple = get_parse_attrs(line)
            # записываем результат парсинга в новый файл, что бы было легче анализировать
            fw.write(f'{str(*parsed_tuple)}\n')
