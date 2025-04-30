# Задание 1
    Напишите на Python библиотеку для поставки внешним клиентам, которая умеет вычислять площадь круга по радиусу и 
    треугольника по трем сторонам. 
    Дополнительно к работоспособности оценим:
    Юнит-тесты
    Легкость добавления других фигур
    Вычисление площади фигуры без знания типа фигуры в compile-time
    Проверку на то, является ли треугольник прямоугольным

#### Пример использования

```python
from shapes_area.shapes import Circle, Triangle, calculate_area, is_right_angled

if __name__ == '__main__':
    circle = Circle(5)
    triangle = Triangle(3, 4, 5)

    print(f"Площадь круга: {calculate_area(circle)}")
    print(f"Площадь треугольника: {calculate_area(triangle)}")
    print(f"Треугольник прямоугольный? {is_right_angled(triangle)}")
    print(f"Круг прямоугольный? {is_right_angled(circle)}")  
```