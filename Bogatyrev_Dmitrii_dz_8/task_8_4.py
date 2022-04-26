from functools import wraps


def val_checker(checking_fun):
    def logger(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Переберем аргументы и применим к ним функцию
            for i in args:
                if not checking_fun(i):
                    # Если проверка не прошла - выкинем ошибку
                    raise ValueError(f'wrong value {i}')
            return func(*args, **kwargs)

        return wrapper

    return logger


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


a = calc_cube(5)
print(a)

a = calc_cube(-5)
print(a)
