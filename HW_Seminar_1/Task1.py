# Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

print("Найдите сумму цифр трехзначного числа.")
num = int(input("Введите трёхзначное число: "))

# Вариант 1 (математическое решение):
a = num // 100
b = num // 10 % 10
c = num % 10
result = a + b + c
print(result)
# print((num // 100) + (num // 10 % 10) + (num % 10))     # вывод в одну строку


# Вариант 2 (if/else):
# if len(str(num)) == 3:
#     print((num // 100) + (num // 10 % 10) + (num % 10))

#     # str_num = str(num)                          # сложение через индексы
#     # print(int(str_num[0]) + int(str_num[1]) + int(str_num[2]))
# else:
#     print("Ошибка! Вы ввели не трёхзначное число! Попробуйте снова.")


# # Вариант 3 (цикл for):
# result = 0
# str_num = str(num)
# for i in range(len(str_num)):
#     result += int(str_num[i])

# print(result)
