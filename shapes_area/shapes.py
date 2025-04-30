import math
from abc import ABC, abstractmethod
from typing import Union


class Shape(ABC):
    """
    Абстрактный базовый класс для геометрических фигур
    """

    @abstractmethod
    def area(self) -> float:
        """
        Вычисляет площадь фигуры
        """
        pass

    @abstractmethod
    def is_right_angled(self) -> bool:
        """
        Проверяет, является ли фигура прямоугольной (если применимо)
        """
        pass


class Circle(Shape):
    """
    Класс для представления круга
    """

    def __init__(self, radius: float):
        """
        Инициализирует круг с заданным радиусом

        :radius: Радиус круга (должен быть положительным)
        :raises: бросает ValueError если радиус меньше или равен нулю
        """
        if radius <= 0:
            raise ValueError("Радиус должен быть положительным числом")
        self.radius = radius

    def area(self) -> float:
        """
        Вычисляет площадь круга по формуле πr²
        """
        return math.pi * self.radius ** 2

    def is_right_angled(self) -> bool:
        """
        Круг не может быть прямоугольным, всегда возвращает False
        """
        return False


class Triangle(Shape):
    """
    Класс для представления треугольника
    """

    def __init__(self, side_a: float, side_b: float, side_c: float):
        """
        Инициализирует треугольник с тремя сторонами

        :side_a: Длина первой стороны
        :side_b: Длина второй стороны
        :side_c: Длина третьей стороны
        :raises: бросает ValueError если стороны не образуют допустимый треугольник
        """
        sides = [side_a, side_b, side_c]
        if any(side <= 0 for side in sides):
            raise ValueError("Все стороны должны быть положительными числами")

        sides_sorted = sorted(sides)
        if sides_sorted[0] + sides_sorted[1] <= sides_sorted[2]:
            raise ValueError("Сумма двух меньших сторон должна быть больше третьей стороны")

        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def area(self) -> float:
        """
        Вычисляет площадь треугольника по формуле Герона
        """
        s = (self.side_a + self.side_b + self.side_c) / 2
        return math.sqrt(s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c))

    def is_right_angled(self) -> bool:
        """
        Проверяет, является ли треугольник прямоугольным по теореме Пифагора
        """
        sides = sorted([self.side_a, self.side_b, self.side_c])
        return math.isclose(sides[0] ** 2 + sides[1] ** 2, sides[2] ** 2, rel_tol=1e-9)


def calculate_area(shape: Union[Circle, Triangle]) -> float:
    """
    Вычисляет площадь фигуры без знания её типа в compile-time

    :shape: Экземпляр класса фигуры (Circle, Triangle или другой Shape)
    :return:Площадь фигуры
    """
    return shape.area()


def is_right_angled(shape: Union[Circle, Triangle]) -> bool:
    """
    Проверяет, является ли фигура прямоугольной (если применимо)

    :shape: Экземпляр класса фигуры (Circle, Triangle или другой Shape)
    :return: True, если фигура прямоугольная, False в противном случае
    """
    return shape.is_right_angled()