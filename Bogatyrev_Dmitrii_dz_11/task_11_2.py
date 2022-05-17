class ZeroDivisionErrorCustom(Exception):
    def __init__(self, txt):
        self.txt = txt


first_number = input("Введите делимое:")
second_number = input("Введите делитель:")

try:
    first_number_int = int(first_number)
    second_number_int = int(second_number)
    if second_number_int == 0:
        raise ZeroDivisionErrorCustom("На ноль делить нельзя!")
except ValueError:
    print("Вы ввели не то число")
except ZeroDivisionErrorCustom as err:
    print(err.txt)
else:
    print(first_number_int / second_number_int)
