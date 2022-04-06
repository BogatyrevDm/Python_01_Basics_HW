original_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха',
                 'была', '+5', 'градусов']
final_list = []
for i in original_list:
    if i.isdigit():  # определим числа без плюса
        if len(i) < 2:  # если число одноразрядное - прибавим 0
            final_list.append('"')
            final_list.append("0" + i)
            final_list.append('"')
        else:  # если нет - поместим в список как есть
            final_list.append('"')
            final_list.append(i)
            final_list.append('"')
    elif i[0] == "+" and i[
                         1:].isdigit():  # если первый знак в строке +, отрежем его и посмотрим, являются ли числом оставшиеся символы
        # если попадется двузначное число с плюсом, результат будет не верный, но в примере этого нет, оставлю так.
        final_list.append('"')
        final_list.append(i[0] + "0" + i[1:])
        final_list.append('"')
    else:
        final_list.append(i)
# При таком способе создается минимальное количество объектов, но между кавычками и числами остаются пробелы
print(" ".join(final_list))

# При таком способе создается больше объектов, он не универсален (если изменится первоначальный список),
# но мы избавляемся от пробелов между кавычками и числами
print(" ".join(final_list[0:2]) + " ".join(final_list[2:3]) + " ".join(final_list[3:6]) + " ".join(
    final_list[6:7]) + " ".join(final_list[7:13]) + " ".join(final_list[13:14]) + " ".join(final_list[14:]))
