# Реализую через словарь. Хранить буду снаружи процедуры в основном коде.
# Это позволит не создавать заново словарь при каждом вызове функции
# Я бы на свой вкус передавал словарь как параметр функции,
# но в шаблоне функции, который предлагается использовать для примера это не предусмотрено

numbers_dictionary = {"zero": "ноль", "one": "один", "two": "два", "three": "три", "four": "четыре", "five": "пять",
                      "six": "шесть", "seven": "семь", "eight": "восемь", "nine": "девять", "ten": "десять"}


def num_translate_adv(value: str) -> str:
    """переводит числительное с английского на русский """

    str_out = numbers_dictionary.get(value.lower(), str(None))
    # Если первый символ - заглавная буква, сделаем результат заглавным
    if value[0].isupper():
        str_out = str_out.capitalize()
    return str_out


print(num_translate_adv("One"))
print(num_translate_adv("two"))
print(num_translate_adv("three"))
print(num_translate_adv("Four"))
print(num_translate_adv("five"))
print(num_translate_adv("six"))
print(num_translate_adv("seven"))
print(num_translate_adv("eight"))
print(num_translate_adv("nine"))
print(num_translate_adv("ten"))
print(num_translate_adv("eleven"))
print(num_translate_adv("Twelve"))
