def percent_declension(percent: int) -> str:
    last_numeric = percent % 10
    if last_numeric == 1 and percent != 11:
        return f'{percent} процент'
    elif (last_numeric == 2 or last_numeric == 3 or last_numeric == 4) and percent != 12 and percent != 13 and percent != 14:
        return f'{percent} процента'
    else:
        return f'{percent} процентов'


for i in range(1, 101):
    result = percent_declension(i)
    print(result)
