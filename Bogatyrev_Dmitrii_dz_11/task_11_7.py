# Я ни разу не математик, поэтому информацию о комплексных числах и правилах их сложения и умножения черпал из этого видео:
# https://www.youtube.com/watch?v=KDllaPIcJcQ
class ComplexNumber:
    # Комплексное число имеет форму c = a + bi
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f'{self.a} + {self.b}*i'

    # при сложении комплексного числа необходимо сложить соответственно обе его части
    def __add__(self, other):
        return ComplexNumber(self.a + other.a, self.b + other.b)

    # при умножении комплексных чисел необходимо перемножить между собой все его члены:
    # (a1 + b1i)*(a2 + b2i)
    def __mul__(self, other):
        return ComplexNumber(self.a * other.a - self.b * other.b, self.a * other.b + self.b * other.a)


first_number = ComplexNumber(7, 3)
second_number = ComplexNumber(6, 2)

third_number = first_number + second_number
print(third_number)

fourth_number = first_number * second_number
print(fourth_number)
