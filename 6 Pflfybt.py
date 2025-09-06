student = {
    "name": 'Григорий Лепс',
    "age": 25,
    "course": "4",
    "grades": [4, 5, 3, 4, 5]
}
print('Информация о студенте')
print(f"Имя, {student['name']} {student['course']} курс ")
print(f"Средний балл студента {sum(student["grades"]) / len(student["grades"])}")
student['grades'].append(5)
print('Оценка 5 добавлена')
print("\nОбновлённая информация о студенте:")
for key, value in student.items():
    print(f"{key}: {value}")


