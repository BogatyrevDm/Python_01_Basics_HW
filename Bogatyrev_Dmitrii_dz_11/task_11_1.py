class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def get_date_parts(cls, date):
        date_parts_list = Date.get_date_as_list(date)
        return date_parts_list[0], date_parts_list[1], date_parts_list[2]

    @staticmethod
    def check_date(date):
        date_parts_list = Date.get_date_as_list(date)
        day = date_parts_list[0]
        month = date_parts_list[1]
        year = date_parts_list[2]
        # Определим високосный год
        long_february_year = year % 4 == 0
        # Месяц должен быть в промежутке от 1 до 12
        if month not in range(1, 13):
            # raise ValueError(f"Wrong month format for month {month}!")
            print(f"Wrong month format for date {date}!")
        # Число дней должно быть не больше 31 одно или 30 в зависимости от месяца, за исключением февраля
        elif month in [1, 3, 5, 7, 8, 10, 12] and day not in range(1, 32) or month in [4, 6, 9,
                                                                                       11] and day not in range(1, 31):
            # raise ValueError(f"Wrong day format for day {day}!")
            print(f"Wrong day format for date {date}!")
        # Проверим число дней в феврале, в зависимости от того, високосный он или нет
        elif month == 2 and (
                long_february_year and day not in range(1, 30) or not long_february_year and day not in range(1, 29)):
            # raise ValueError(f"Wrong day format for day {day}!")
            print(f"Wrong day format for date {date}!")

    @staticmethod
    def get_date_as_list(date):
        date_parts_list = list(map(int, date.split("-")))
        if len(date_parts_list) < 3:
            raise ValueError("Wrong format!")
        return date_parts_list


first_date = Date('1-12-2021')
print(*Date.get_date_parts(first_date.date))
# Проверка пройдет
Date.check_date(first_date.date)

second_date = Date('1-22-2021')
print(*Date.get_date_parts(second_date.date))
# Месяц больше 12
Date.check_date(second_date.date)

third_date = Date('12-2-2022')
print(*Date.get_date_parts(third_date.date))
# Проверка пройдет
Date.check_date(third_date.date)

wrong_date_1 = Date('32-1-2022')
print(*Date.get_date_parts(wrong_date_1.date))
# 32 дня в январе
Date.check_date(wrong_date_1.date)

wrong_date_2 = Date('31-4-2022')
print(*Date.get_date_parts(wrong_date_2.date))
# 31 день в апреле
Date.check_date(wrong_date_2.date)

wrong_date_3 = Date('29-2-2022')
print(*Date.get_date_parts(wrong_date_3.date))
# 29 дней в феврале невисокосного года
Date.check_date(wrong_date_3.date)
