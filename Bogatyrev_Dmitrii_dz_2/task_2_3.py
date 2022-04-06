original_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха',
                 'была', '+5', 'градусов']
# Переберем список к конца, что бы вставка кавычек не сбила индексацию
for i in range(len(original_list) - 1, 0, -1):
    list_item = original_list[i]
    if list_item.isdigit():
        if len(list_item) < 2:  # определим числа без плюса
            original_list[i] = "0" + list_item
        # Вставим кавычку после числа и перед
        original_list.insert(i + 1, '"')
        original_list.insert(i, '"')
    elif list_item[0] == "+" and list_item[
                                 1:].isdigit():  # если первый знак в строке +, отрежем его и посмотрим, являются ли числом оставшиеся символы
        # если попадется двузначное число с плюсом, результат будет не верный, но в примере этого нет, оставлю так.
        original_list[i] = list_item[0] + "0" + list_item[1:]
        # Вставим кавычку после числа и перед
        original_list.insert(i + 1, '"')
        original_list.insert(i, '"')

# При таком способе создается минимальное количество объектов, но между кавычками и числами остаются пробелы
print(" ".join(original_list))

# При таком способе создается больше объектов, он не универсален (если изменится первоначальный список),
# но мы избавляемся от пробелов между кавычками и числами
print(" ".join(original_list[0:2]) + " ".join(original_list[2:3]) + " ".join(original_list[3:6]) + " ".join(
    original_list[6:7]) + " ".join(original_list[7:13]) + " ".join(original_list[13:14]) + " ".join(original_list[14:]))
