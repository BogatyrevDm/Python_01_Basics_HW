import re

# Регулярное выражения для валидации
RE_VALIDATION = re.compile(r'^([A-Za-z0-9-_.]+)@([A-Za-z]+)\.([A-z]+)$')

# Регулярное выражения для разделения
RE_SEPARATION = re.compile(r'(?P<username>[A-Za-z0-9]+)(?=@)@(?<=@)(?P<domain>[A-Za-z.]+)')


def email_parse(email_address):
    # Если адрес валиден - вернем словарь
    if RE_VALIDATION.match(email_address):
        return (map(lambda x: x.groupdict(), RE_SEPARATION.finditer(email_address)))
    # В противном случае - выбросим исключение
    else:
        raise ValueError(f'wrong email:{email_address}')


print(*email_parse("someone@geekbrains.com"))
print(*email_parse("someonegeekbrains.com"))
print(*email_parse("someone@geekbrainscom"))
print(*email_parse("someone@g666eekbrains.com"))
print(*email_parse("bsomeone@geekbrains.888com"))
