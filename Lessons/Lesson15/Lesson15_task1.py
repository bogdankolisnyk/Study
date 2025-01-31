import math

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        """Метод для обчислення площі прямокутника."""
        return self.width * self.height

    def __eq__(self, other):
        """Метод для порівняння двох прямокутників за площею."""
        if isinstance(other, Rectangle):
            return self.get_square() == other.get_square()
        return False

    def __add__(self, other):
        """Метод для додавання двох прямокутників. Площа нового прямокутника дорівнює сумі площ обох."""
        if isinstance(other, Rectangle):
            total_area = self.get_square() + other.get_square()
            new_width = total_area / self.height
            return Rectangle(new_width, self.height)
        return NotImplemented

    def __mul__(self, n):
        """Метод для множення прямокутника на число. Площа нового прямокутника збільшується в n разів."""
        if isinstance(n, (int, float)):
            new_area = self.get_square() * n
            new_height = new_area / self.width
            return Rectangle(self.width, new_height)
        return NotImplemented

    def __str__(self):
        """Метод для отримання рядкового представлення прямокутника."""
        return f"Rectangle(width={self.width}, height={self.height})"

r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)

assert r1.get_square() == 8, 'Test1'
assert r2.get_square() == 18, 'Test2'

r3 = r1 + r2
assert r3.get_square() == 26, 'Test3'

r4 = r1 * 4
assert r4.get_square() == 32, 'Test4'
assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'

print(r3)
print(r4)