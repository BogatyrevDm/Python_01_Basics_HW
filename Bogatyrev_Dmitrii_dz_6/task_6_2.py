with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:
    # словарь, в котором ключи - ip пользователя, значения = количество запросов
    ip_dict = {}
    # перебираем список и парсим каждую строку
    for line in fr:
        # получим список из строки, очищенной от пробелов
        line_listed = line.strip().split()
        # первый элемент списк - ip пользователя
        user_ip = line_listed[0]
        # поместим его в словарь, установив количество запросов = 0, в случае, когда его там нет
        default_count = ip_dict.setdefault(user_ip, 0)
        # увеличим количество запросов на 1
        ip_dict[user_ip] = default_count + 1
    # хранит значение максимального количество обращений к серверу
    max_value = 0
    # хранит значение IP пользователя, который обратился к серверу максимальное количество раз
    max_user_ip = ""
    # переберем словарь, сравнивая следующее значение с предыдущим
    for key, value in ip_dict.items():
        if value > max_value:
            max_value = value
            max_user_ip = key
    print(f'IP {max_user_ip} called the server {max_value} times')
