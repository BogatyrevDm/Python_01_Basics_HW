from requests import get, utils


def currency_rates(code: str) -> float:
    """возвращает курс валюты `code` по отношению к рублю"""
    response = get("https://www.cbr.ru/scripts/XML_daily.asp")

    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encodings)
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

    return result_value


print(currency_rates("usd"))
print(currency_rates("USD"))
print(currency_rates("eur"))
print(currency_rates("EUR"))
print(currency_rates("noname"))
