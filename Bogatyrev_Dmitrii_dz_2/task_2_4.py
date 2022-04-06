raw_data = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй',
            'директор аэлита']
# Вариант с промежуточным списком
for i in raw_data:
    _words = i.split(' ')
    print(f'Привет, {_words[-1].capitalize()}!')
# Вариант без промежуточного списка
for i in raw_data:
    # Реверсируем строку
    _reversed_data = i[::-1]
    # Найдем первое слово
    _reversed_name = _reversed_data[:_reversed_data.index(' ')]
    # Вернем нормальный порядок букв и приведем к необходимому виду
    _capitalized_name = _reversed_name[::-1].capitalize()
    print(f'Привет, {_capitalized_name}!')
