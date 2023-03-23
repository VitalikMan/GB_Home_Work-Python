# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа.
# n - кол-во элементов первого множества.
# m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

import random

size_set_one = int(input("Введите количество первого множества: "))
size_set_two = int(input("Введите количество второго множества: "))

min_val = int(input("Введите min числовой диапазон чисел во множестве: "))
max_val = int(input("Введите max числовой диапазон чисел во множестве: "))
if min_val > max_val:
    min_val, max_val = max_val, min_val

set_one = set()
set_two = set()

for i in range(size_set_one):
    i = random.randint(min_val, max_val)
    set_one.add(i)

for i in range(size_set_two):
    i = random.randint(min_val, max_val)
    set_two.add(i)

print(set_one)
print(set_two)

set_three = set_one.union(set_two)
print(set_three)

print(sorted(set_three))
