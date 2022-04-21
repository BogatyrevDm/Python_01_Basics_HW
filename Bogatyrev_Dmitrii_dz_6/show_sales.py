def read_prices(first_position=-1, last_position=-1):
    # открываем файл на чтение
    with open('bakery.csv', 'r', encoding='utf-8') as fr:
        for i, line in enumerate(fr):
            if first_position >= 0:
                if i >= first_position:
                    if last_position > 0:
                        if i <= last_position:
                            print(line.strip())
                    else:
                        print(line.strip())
            else:
                price = line.strip()
                print(price)


if __name__ == '__main__':
    import sys

    if type(sys.argv) == list:
        # если параметры не переданы - выводим все значения
        if len(sys.argv) == 1:
            read_prices()
        else:
            program, *args = sys.argv
            # передан один параметр
            if len(args) == 1:
                read_prices(int(args[0]) - 1)
            # передано 2 параметра
            elif len(args) == 2:
                read_prices(int(args[0]) - 1, int(args[1]) - 1)
