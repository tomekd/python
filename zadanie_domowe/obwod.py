"""
Zaimplementuj funkcję `obwod`,obliczy i zwróci obwód zadanej figury. 
Szablon funkcji znajduje się poniżej. Funkcja przyjmuje dokładnie 1 argument, będący listą 2-elementowych krotek
oznaczającymi współrzędne x i y wierzchołka.

Przykład:
obwod([(0,0), (0,1), (1,1), (1,0)]) == 4
"""
import math


def obwod(points):
    perimeter = 0
    for i, point in enumerate(points):
        perimeter += math.dist(point, points[(i + 1) % len(points)])
    return perimeter


print(obwod([(0, 0), (0, 1), (1, 1), (1, 0)]))
