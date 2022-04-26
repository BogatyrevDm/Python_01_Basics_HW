from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        # Получим список строк неименованных аргументов
        logger_result_args = map(lambda i: f'{i}: {type(i)}', args)

        # Получим список строк именованных аргументов
        logger_result_kwargs = map(lambda i: f'{i[1]}: {type(i[1])}', kwargs.items())
        # Тип значения функции
        print(type(func))
        # Залогируем аргументы и имя функции
        print(f'{func.__name__} ({", ".join(logger_result_args)}, {", ".join(logger_result_kwargs)})')
        return result

    return wrapper


# Аргументы не используются, добавлены для демонстрации работы декоратора
@type_logger
def calc_cube(x, y, z):
    return x ** 3


a = calc_cube(5, 6, z="4")
