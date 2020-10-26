class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __abs__(self):
        return (self.imaginary ** 2 + self.real ** 2) ** 0.5

    def __add__(self, other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imaginary - other.imaginary)

    def __mul__(self, other):
        real = self.real * other.real - self.imaginary * other.imaginary
        im = self.real * other.imaginary + other.real * self.imaginary
        return Complex(real, im)

    def __truediv__(self, other):
        chisl = self * other.sopr()
        real = chisl.real / (abs(other) ** 2)
        im = chisl.imaginary / (abs(other) ** 2)
        return Complex(real, im)

    def __str__(self):
        return f'({self.real}, {self.imaginary})'

    def sopr(self):
        return Complex(self.real, -self.imaginary)


a = Complex(1, 1)
b = Complex(1, 1)
print(a / b)
