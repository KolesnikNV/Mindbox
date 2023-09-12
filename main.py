import math
from typing import List, Union


class TriangleValidator:
    @staticmethod
    def is_valid_triangle(side1: float, side2: float, side3: float) -> List[float]:
        """
        Проверяет, являются ли заданные длины сторон корректными для треугольника.
        """
        if side1 <= 0 or side2 <= 0 or side3 <= 0:
            raise ValueError("Длины сторон должны быть положительными числами")
        sides = [side1, side2, side3]
        if sides[0] + sides[1] <= sides[2]:
            raise ValueError("Такой треугольник не может существовать!")
        return sides


class GeometryCalculator:
    @staticmethod
    def circle_area(radius: float) -> float:
        """
        Вычисляет площадь круга по заданному радиусу.
        """
        if radius <= 0:
            raise ValueError("Радиус должен быть положительным числом")
        return math.pi * radius**2

    @staticmethod
    def triangle_area(side1: float, side2: float, side3: float) -> float:
        """
        Вычисляет площадь треугольника по длинам его сторон.
        """
        if sides := TriangleValidator.is_valid_triangle(side1, side2, side3):
            s = sum(sides) / 2
            return math.sqrt(s * (s - side1) * (s - side2) * (s - side3))

    @staticmethod
    def rectangle_area(length: float, width: float) -> float:
        """
        Вычисляет площадь прямоугольника по его длине и ширине.
        """
        if length <= 0 or width <= 0:
            raise ValueError("Длина и ширина должны быть положительными числами")
        return length * width

    @staticmethod
    def square_area(side: float) -> float:
        """
        Вычисляет площадь квадрата по длине его стороны.
        """
        if side <= 0:
            raise ValueError("Длина стороны квадрата должна быть положительным числом")
        return side**2

    @staticmethod
    def is_right_triangle(side1: float, side2: float, side3: float) -> bool:
        """
        Проверяет, является ли треугольник прямоугольным.
        """
        if sides := TriangleValidator.is_valid_triangle(side1, side2, side3):
            sides.sort()
            return abs(sides[0] ** 2 + sides[1] ** 2 - sides[2] ** 2) < 1e-6

    @staticmethod
    def calculate_area(**kwargs: Union[float, int]) -> float:
        """
        Вычисляет площадь геометрической фигуры на основе переданных параметров.
        """
        if "radius" in kwargs:
            return GeometryCalculator.circle_area(float(kwargs["radius"]))
        elif all(key in kwargs for key in ("side1", "side2", "side3")):
            return GeometryCalculator.triangle_area(
                float(kwargs["side1"]), float(kwargs["side2"]), float(kwargs["side3"])
            )
        elif all(key in kwargs for key in ("length", "width")):
            return GeometryCalculator.rectangle_area(
                float(kwargs["length"]), float(kwargs["width"])
            )
        elif "side" in kwargs:
            return GeometryCalculator.square_area(float(kwargs["side"]))
        else:
            raise ValueError("Неверные аргументы")


def main():
    radius = 5
    side1 = 3
    side2 = 4
    side3 = 5
    length = 8
    width = 6
    square_side = 4

    calculator = GeometryCalculator()

    circle_area = calculator.circle_area(radius)
    print(f"Площадь круга с радиусом {radius}: {circle_area:.2f}")

    triangle_area = calculator.triangle_area(side1, side2, side3)
    print(
        f"Площадь треугольника со сторонами {side1}, {side2}, {side3}: {triangle_area:.2f}"
    )
    rectangle_area = calculator.rectangle_area(length, width)
    print(
        f"Площадь прямоугольника с длиной {length} и шириной {width}: {rectangle_area:.2f}"
    )
    square_area = calculator.square_area(square_side)
    print(f"Площадь квадрата со стороной {square_side}: {square_area:.2f}")

    is_right = calculator.is_right_triangle(side1, side2, side3)
    print(
        f"Треугольник со сторонами {side1}, {side2}, {side3} является прямоугольным: {is_right}"
    )

    area1 = calculator.calculate_area(radius=radius)
    area2 = calculator.calculate_area(side1=side1, side2=side2, side3=side3)
    area3 = calculator.calculate_area(length=length, width=width)
    area4 = calculator.calculate_area(side=square_side)
    print(f"Площадь круга: {area1:.2f}")
    print(f"Площадь треугольника: {area2:.2f}")
    print(f"Площадь прямоугольника: {area3:.2f}")
    print(f"Площадь квадрата: {area4:.2f}")


# Вывод:
# Площадь круга с радиусом 5: 78.54
# Площадь треугольника со сторонами 3, 4, 5: 6.00
# Площадь прямоугольника с длиной 8 и шириной 6: 48.00
# Площадь квадрата со стороной 4: 16.00
# Треугольник со сторонами 3, 4, 5 является прямоугольным: True
# Площадь круга: 78.54
# Площадь треугольника: 6.00
# Площадь прямоугольника: 48.00
# Площадь квадрата: 16.00

if __name__ == "__main__":
    main()
