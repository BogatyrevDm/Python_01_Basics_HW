def write_price(price):
    # Откроем файл в режиме дозаписи
    with open('bakery.csv', 'a', encoding='utf-8') as fa:
        # Запищем цену в конец файла с переводом строки
        fa.write(f'{price}\n')


if __name__ == '__main__':
    import sys

    if type(sys.argv) == list and len(sys.argv) > 1:
        program, price = sys.argv
        write_price(price)

