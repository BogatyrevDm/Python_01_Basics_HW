class Cell():
    def __init__(self, quantity):
        self.quantity = quantity

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity):
        if type(quantity) is not int:
            raise ValueError("Wrong type!")
        self.__quantity = quantity

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        sub_value = self.quantity - other.quantity
        if sub_value < 0:
            raise ValueError("The result is sub zero!")
        return Cell(sub_value)

    def __mul__(self, other):
        return Cell(self.quantity * other.quantity)

    def __floordiv__(self, other):
        return Cell(self.quantity // other.quantity)

    def make_order(self, raw_count):
        quantity = self.quantity
        quantity_list = []
        current_row_count = 0
        if quantity < raw_count:
            raw_count = quantity
        for i in range(max(quantity, raw_count)):
            if current_row_count == raw_count:
                quantity_list.append("\n")
                current_row_count = 0
            quantity_list.append("*")
            current_row_count += 1
        print("".join(quantity_list))


first_cell = Cell(3)
second_cell = Cell(10)

add_cell = first_cell + second_cell
Cell.make_order(add_cell, 5)
print()
sub_sell = second_cell - first_cell
Cell.make_order(sub_sell, 5)
print()
mult_sell = first_cell * second_cell
Cell.make_order(mult_sell, 5)
print()
floor_div_cell = second_cell // first_cell
Cell.make_order(floor_div_cell, 5)
