def sum_list_1(dataset: list) -> int:
    result = 0
    for i in dataset:
        end_of_number = i
        number_sum = 0
        while end_of_number > 0:
            first_part = end_of_number // 10  # делим число нацело на 10, отбрасывая таким образом последний разряд
            number_sum += end_of_number % 10  # получаем с конца последовательно все цифры и суммируем их

            end_of_number = first_part
            if first_part == 0:  # если поделили нацело на 10 и получили ноль - достигнут последний разряд, цикл можно закончить
                end_of_number = 0
        if number_sum % 7 == 0:
            result += i

    return result


def sum_list_2(dataset: list) -> int:
    result = 0
    for i in dataset:
        end_of_number = i + 17  # прибавляем к исходному числу 17
        number_sum = 0
        while end_of_number > 0:
            first_part = end_of_number // 10  # делим число нацело на 10, отбрасывая таким образом последний разряд
            number_sum += end_of_number % 10  # получаем с конца последовательно все цифры и суммируем их

            end_of_number = first_part
            if first_part == 0:  # если поделили нацело на 10 и получили ноль - достигнут последний разряд, цикл можно закончить
                end_of_number = 0
        if number_sum % 7 == 0:
            result += i + 17

    return result


my_list = []
for i in range(1, 1001):
    if i % 2 != 0:
        my_list.append(i ** 3)

result_1 = sum_list_1(my_list)
print(result_1)
result_2 = sum_list_2(my_list)
print(result_2)
