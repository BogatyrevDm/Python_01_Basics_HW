from itertools import zip_longest


class Matrix:
    def __init__(self, param):
        self.param = param

    def __str__(self):
        result = ""
        for i in self.param:
            result += f'{" ".join(map(str, i))}\n'
        return result.strip()

    def __add__(self, other):
        def return_zero_if_none(value):
            """
            вспомогательная процедура, которая возвращает 0, если переданное значение None
            """
            if value is None:
                value = 0
            return value

        result = []
        # переберем первый уровень матрицы
        for first_list, second_list in zip_longest(self.param, other.param):
            result_inner_list = []
            # переберем второй уровень матрицы
            for first_inner_list, second_inner_list in zip_longest(first_list, second_list):
                # сложим значение и создадим второй уровень новой матрицы
                result_inner_list.append(return_zero_if_none(first_inner_list) + return_zero_if_none(second_inner_list))
            # добавим второй уровень новой матрицы
            result.append(result_inner_list)
        return Matrix(result)


first_matrix = Matrix([[31, 22], [37, 43], [51, 86]])
print(first_matrix)
second_matrix = Matrix([[3, 5, 32], [2, 46, 6], [-1, 64, -8]])
print(second_matrix)
third_matrix = first_matrix + second_matrix
print(third_matrix)
