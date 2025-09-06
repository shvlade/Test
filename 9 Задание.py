import random
numbers = [random.randint(-10, 10) for _ in range(15)]
print(numbers)
pol = [num for num in numbers if num > 0]
print(pol)
x2 = [num ** 2 for num in numbers]
print(x2)