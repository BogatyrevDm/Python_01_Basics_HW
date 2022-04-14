import utils

currencies_list = ["usd", "USD", "eur", "EUR", "noname"]

for i in currencies_list:
    kurs, date_value = utils.currency_rates_adv(i)
    utils.check_values(kurs, date_value)
    print(kurs, date_value)

'''
Результат выполнения в консоли:
79.8471 2022-04-14
79.8471 2022-04-14
86.7219 2022-04-14
86.7219 2022-04-14
Traceback (most recent call last):
  File "F:\Python_workspaces\GB_Python_01_Basics\HW\Bogatyrev_Dmitrii_dz_4\task_4_3.py", line 54, in <module>
    check_values(kurs, date_value)
  File "F:\Python_workspaces\GB_Python_01_Basics\HW\Bogatyrev_Dmitrii_dz_4\task_4_3.py", line 45, in check_values
    raise TypeError("Неверный тип данных у курса")
TypeError: Неверный тип данных у курса

Process finished with exit code 1

'''