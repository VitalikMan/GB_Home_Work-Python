# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

number = int(
    input("Введите число, до которого нужно вывести все степени двойки: "))


for i in range(number+1):           # <-- Вариант 1 (for)
    if 2**i <= number:
        print(2**i)


# i = 0                               # <-- Вариант 2 (while)
# while 2**i <= number:
#     print(2**i)
#     i += 1