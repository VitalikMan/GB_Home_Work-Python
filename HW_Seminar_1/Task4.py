# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no

print("Давайте проверим, можно ли разломить шоколадку на два прямоугольника)")
chocolate_length = int(input("Введите длину шоколада: "))
chocolate_width = int(input("Введите ширину шоколада: "))
slices = int(input("Введите количество долек, которое необходимо отломить: "))

total_number_of_slices = chocolate_length * chocolate_width

result = total_number_of_slices - slices

if result % 2 == 0:
    print("Да! Можно разломить шоколадку на два прямоугольника. УРА! :)")
else:
    print("К сожалению, нет.. :(")
