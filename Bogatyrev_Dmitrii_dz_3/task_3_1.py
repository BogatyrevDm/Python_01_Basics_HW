# Реализую через словарь. Хранить буду снаружи процедуры в основном коде.
# Это позволит не создавать заново словарь при каждом вызове функции
# Я бы на свой вкус передавал словарь как параметр функции,
# но в шаблоне функции, который предлагается использовать для примера это не предусмотрено

numbers_dictionary = {"zero": "ноль", "one": "один", "two": "два", "three": "три", "four": "четыре", "five": "пять",
                      "six": "шесть", "seven": "семь", "eight": "восемь", "nine": "девять", "ten": "десять"}


def num_translate(value: str) -> str:
    """переводит числительное с английского на русский """

    str_out = numbers_dictionary.get(value, None)
    return str_out


print(num_translate("one"))
print(num_translate("two"))
print(num_translate("three"))
print(num_translate("four"))
print(num_translate("five"))
print(num_translate("six"))
print(num_translate("seven"))
print(num_translate("eight"))
print(num_translate("nine"))
print(num_translate("ten"))
print(num_translate("eleven"))
print(num_translate("twelve"))
