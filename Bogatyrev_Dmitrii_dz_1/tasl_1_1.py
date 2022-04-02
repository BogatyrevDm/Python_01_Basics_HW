def convert_time(duration: int) -> str:
    seconds_in_minute = 60
    seconds_in_hour = 3600
    seconds_in_day = 86400
    if duration <= 0:  # передали ноль или отрицательное число
        return f'Невозможно конвертировать число'
    elif duration <= seconds_in_minute:  # в минуте 60 секунд
        return f'{duration} сек'
    elif duration <= seconds_in_hour:  # в часе 3600 секунд
        minutes = duration // seconds_in_minute
        seconds = duration % seconds_in_minute
        return f'{minutes} мин {seconds} сек'
    elif duration <= seconds_in_day:  # в сутках 86400 секунд
        hours = duration // seconds_in_hour
        minutes = duration % seconds_in_hour // seconds_in_minute
        seconds = duration % seconds_in_hour % seconds_in_minute
        return f'{hours} час {minutes} мин {seconds} сек'
    else:
        days = duration // seconds_in_day
        hours = (duration % seconds_in_day) // seconds_in_hour
        minutes = duration % seconds_in_day % seconds_in_hour // seconds_in_minute
        seconds = duration % seconds_in_day % seconds_in_hour % seconds_in_minute
        return f'{days} дн {hours} час {minutes} мин {seconds} сек'


durations = [-2, 1, 35, 59, 61, 68, 3599, 3601, 50256, 86399, 86401, 900000]
for duration in durations:
    result = convert_time(duration)
    print(result)
'''Правильные результаты для введенных длительностей:
Невозможно конвертировать число
1 сек
35 сек
59 сек
1 мин 1 сек
1 мин 8 сек
59 мин 59 сек
1 час 0 мин 1 сек
13 час 57 мин 36 сек
23 час 59 мин 59 сек
1 дн 0 час 0 мин 1 сек
10 дн 10 час 0 мин 0 сек'''
