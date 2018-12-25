
__author__ = 'Zinovyev Alexander Victorovich'

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.

number = str(input("Please, input your number: "))
bigNumber = 0
x = 0

for i in number:
    if int(i) > bigNumber:
        bigNumber = int(i)

# while x < len(number):
#     if int(number[x]) > bigNumber:
#         bigNumber = int(number[x])
#     x += 1

print("Biggest numeral is " + str(bigNumber))

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
# * при желании и понимании воспользуйтесь синтаксисом кортежей Python.

print("Please, input two values")

a = (input("Input first value: "), input("Input second value: "))

print("Let's see'")
print(a)

a = (a[1], a[0])

print("Swapped!" + str(a))



# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4

import math

print("Enter your coefficients")

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

d = int(b**2 - 4 * a * c)
if d > 0:
    x = (-b + math.sqrt(d)) / (2 * a)
elif d < 0:
    print("Вещественных корней нет!")
else:
    x = -b / (2 * a)
print("Root: " + str(x))
