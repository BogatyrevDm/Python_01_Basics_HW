class WrongValueCustom(Exception):
    def __init__(self, txt):
        self.txt = txt


int_list = []
while True:
    result = input(f'Введите числовое значение или stop для остановки:\n')
    # Если ввели "stop" - выведем список и прервем выполнение
    if result == "stop":
        print(int_list)
        break
    try:
        # если введено не число - выбросим кастомную ошибку
        if not result.isdigit():
            raise WrongValueCustom("Результат должен быть числом!")
    # перехватим кастомную ошибку и выведем текст сообщения на экран
    except WrongValueCustom as err:
        print(err.txt)
    # если значение правильное - добавим в список
    else:
        int_list.append(int(result))
