start = int(input())
end = int(input())
num = False
for i in range(start, end + 1):
    if i % 2 == 0:
        print(i)
        num = True
if not num:
    print("В этом диапазоне нет чётных чисел.")