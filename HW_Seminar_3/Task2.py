# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# Пример:
# N = 5 <-- количество элементов в массиве
#     [1, 2, 3, 4, 5]
#     x = 6
#     5 <-- результат

import random

size = int(input("Введите количество элементов в списке: "))
min_range = int(input("Введите минимальный числовой диапазон числа: "))
max_range = int(input("Введите максимальный числовой диапазон числа: "))

my_list = [random.randint(min_range, max_range) for _ in range(size)]
print(my_list)

number = int(input("Введите число: "))

diff = abs(my_list[0] - number)     # разница в значении
closest_value = my_list[0]          # ближайшее значение

for i in range(1, size):
    if abs(my_list[i] - number) < diff:
        diff = abs(my_list[i] - number)
        closest_value = my_list[i]

print(
    f"Ближайший элемент к числу {number} по списку, является {closest_value}")
