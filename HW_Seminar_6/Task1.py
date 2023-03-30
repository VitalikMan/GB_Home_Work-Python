# Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

user_input = list(map(int, input(
    "Введите число, шаг и количество элементов в списке, через пробел: ").split()))


def my_list_1(num: int, step: int, size: int):         # Вариант 1
    my_list = []
    count = 0
    i = num
    while count < size:
        my_list.append(i)
        i += step
        count += 1
    return print(my_list)


my_list_1(user_input[0], user_input[1], user_input[2])


# def my_list_2(num: int, step: int, size: int):        # Вариант 2
#     my_list2 = []
#     for i in range(size):
#         my_list2.append(num + i * step)
#     return print(my_list2)


# my_list_2(user_input[0], user_input[1], user_input[2])
