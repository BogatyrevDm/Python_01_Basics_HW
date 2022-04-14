from datetime import date

from requests import get, utils


def currency_rates_adv(code: str) -> tuple[float | None, date]:
    """возвращает курс валюты `code` по отношению к рублю"""
    response = get("https://www.cbr.ru/scripts/XML_daily.asp")

    encodings = utils.get_encoding_from_headers(response.headers)

    content = response.content.decode(encodings)
    # Найдем позицию тега ValCurs с атрибутом Date
    date_position = content.find("ValCurs Date=")
    # Вырежем дату
    date_value = content[date_position + 14:date_position + 24]

    date_value = date(int(date_value[6:]), int(date_value[3:5]), int(date_value[:2]))

    result_value = None
    # Найдем тег CharCode со значением переданного кода валюты
    val_code_position = content.find(f'CharCode>{code.upper()}')
    if val_code_position != -1:
        # Обрежем файл по найденому тегу
        content = content[val_code_position:]
        value_tag_name = "<Value>"
        # Найдем открывающий тег Value
        value_open_tag_position = content.find(value_tag_name)
        # Найдем закрывающий тег Value
        value_closing_tag_position = content.find("</Value>")
        # Между этими тегами - значение курса
        val_value = content[value_open_tag_position + len(value_tag_name):value_closing_tag_position]
        if val_value != "":
            # Заменим запятую точкой
            result_value = val_value.replace(",", ".")
            # Приведем к float
            result_value = float(result_value)

    return result_value, date_value


def check_values(kurs, date_value):
    empty = bool(not kurs and not date_value)
    if not empty and not isinstance(kurs, float):
        raise TypeError("Неверный тип данных у курса")
    if not empty and not isinstance(date_value, date):
        raise TypeError("Неверный тип данных у даты")


currencies_list = ["usd", "USD", "eur", "EUR", "noname"]

for i in currencies_list:
    kurs, date_value = currency_rates_adv(i)
    check_values(kurs, date_value)
    print(kurs, date_value)
