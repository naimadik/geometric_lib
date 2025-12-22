import math


def area(r):
    '''Возвращает площадь круга
    Пример вызова:
    area(5) вернет 25пи'''
    if r < 0:
        raise ValueError("Радиус не может быть отрицательным")

    return math.pi * r * r


def perimeter(r):
    '''Возвращает длину окружности
    Пример вызова:
    perimetr(5) вернет 10пи'''
    if r < 0:
        raise ValueError("Радиус не может быть отрицательным")
    return 2 * math.pi * r
