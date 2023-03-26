# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# *Пример:*

# 2 2
#     4

number_A = int(input("Введите число A: "))
number_B = int(input("Введите число B: "))


def summa_num(a: int, b: int) -> int:
    if a == 0 and b == 0:
        return 0
    elif a == 0:
        return b
    elif b == 0:
        return a
    else:
        return summa_num(a - 1, b + 1)


print(
    f"Сумма двух чисел {number_A} и {number_B} => {summa_num(number_A, number_B)}")
