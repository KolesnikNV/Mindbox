# Геометрический калькулятор
Этот проект представляет собой геометрический калькулятор, который позволяет вычислять площади различных геометрических фигур, таких как круги, треугольники, прямоугольники и квадраты.

## Установка
Склонируйте репозиторий на свой локальный компьютер:

```git clone https://github.com/KolesnikNV/Mindbox.git```

## Использование
Вы можете использовать геометрический калькулятор, вызывая его методы из Python-скрипта или интерактивного интерпретатора Python.

Пример использования в Python-скрипте:

from main import GeometryCalculator

calculator = GeometryCalculator()
# Вычисление площади круга
circle_area = calculator.circle_area(5)
print(f"Площадь круга: {circle_area:.2f}")
# Вычисление площади треугольника
triangle_area = calculator.triangle_area(3, 4, 5)
print(f"Площадь треугольника: {triangle_area:.2f}")
