# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

arr = ["яблоко", "банан", "киви", "арбуз"]
c = 1

for i in arr:
    print("{}.{:>7}".format(c, i))
    c += 1

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

listA = list()
listB = list()
i = 0

while True:
    listA.append(input("Введите элемент в список А? Закончить - [Q]"))
    if listA[len(listA)-1] == "Q":
        listA.pop()
        break


while True:
    listB.append(input("Введите элемент в список B? Закончить - [Q]"))
    if listB[len(listB)-1] == "Q":
        listB.pop()
        break

# for i in listB:
#     for c in listA:
#         if i == c:
#             listA.remove(c)

for i in listB:
    while listA.count(i) > 0:
        listA.pop(listA.index(i))

print("Массив А без элементов массива В: {}".format(listA))

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

arr = list()
i = 0

while True:
    arr.append(input("Введите элемент в список Закончить - [Q]"))
    if arr[len(arr) - 1] == "Q":
        arr.pop()
        break

print("Изначальный список: {}".format(arr))

while i < len(arr):
    if int(arr[i]) % 2 == 0:
        arr[i] = int(arr[i]) / 4
    else:
        arr[i] = int(arr[i]) * 21
    i += 1
print("Измененный список: {}".format(arr))
