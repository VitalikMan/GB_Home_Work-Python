# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint

size = int(input("Введите размер списка: "))
min_val_rand = int(input("Введите min числовой диапазон чисел в списке: "))
max_val_rand = int(input("Введите max числовой диапазон чисел в списке: "))
if min_val_rand > max_val_rand:
    min_val_rand, max_val_rand = max_val_rand, min_val_rand

my_list = [randint(min_val_rand, max_val_rand) for _ in range(size)]
print(my_list)

min_number = int(input("Введите минимальное значение диапазона: "))
max_number = int(input("Введите максимальное значение диапазона: "))

for i in range(len(my_list)):
    if min_number <= my_list[i] <= max_number:
        print(f'Число {my_list[i]} входит в диапазон и имеет индекс {i}')
