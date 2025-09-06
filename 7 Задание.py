from math import *

def calculate_circle_area(radius):
    return 3.14159 * radius ** 2
def is_positive(number):
    return number > 0
print(f"Площадь круга {calculate_circle_area(5):.2f}")
print(f"Число 19  положительное {is_positive(19)}")