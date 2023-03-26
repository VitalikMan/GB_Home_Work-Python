# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8

number = int(input("Введите число: "))
degree_of_number = int(input("Введите степень числа: "))


def degree_of(number: int, degree_of_number: int) -> int:
    if degree_of_number == 0:
        return 1
    else:
        return number * degree_of(number, degree_of_number - 1)


print(f"Число {number} в степени {degree_of_number} => {degree_of(number, degree_of_number)}")
