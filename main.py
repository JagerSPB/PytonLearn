import math
import random
import sys
import modul_test as m1
from random import randint


# from modul_test import *
# nKmDayly = 700
# mTrack = 750
#
# print(f"Машина может проехать  дней {math.ceil(mTrack / nKmDayly)}")

# a = 20
# b = 21
# c = 23
# print(f"класс A: {(a // 2 + a % 2)} класс B: {b // 2 + b % 2} класс C: {c // 2 + c % 2} ")
# print(f"Всего необходимо {(a // 2 + a % 2) + (b // 2 + a % 2) + (c // 2 + c % 2)}")
#


# print("Enter year for check: ")
# checkYear = int(input())
# if (checkYear % 4 == 0 and checkYear % 100 != 0) or checkYear % 400 == 0:
#     print(f"{checkYear} год високосный")
# else:
#     print(f"{checkYear} год не високосный")

# print("Порядковый номер вагона: ")
# i = int(input())
# print("Номер вагона который в который сел Витя: ")
# j = int(input())
# if (i == j):
#     print("невозможно определить длину поезда")
# else:
#     print(f"В поезде {i + j - 1} вагонов")


# print("number: ")
# i = float(input())
# sum = 0
# sumFloat = 0
# i1 = i % 1
# while i1 > 0:
#     sumFloat += i1 % 10
#     i1 = i1 // 10
# while i > 0:
#     sum += i % 10
#     i = i // 10
#
# print(sumFloat)
# n = 120
#
# # Введите ваше решение ниже
#
# x = n // 6
# p = x
# s = x
# k = 4 * x
# print(f"{p}  {s}  {k}")

#
# n = 385919
#
# # Введите ваше решение ниже
# leftPart = n // 1000
# rightPart = n % 1000
# sumLeft = 0
# while leftPart > 0:
#     sumLeft += leftPart % 10
#     leftPart = leftPart // 10
#
# sumRight = 0
# while rightPart > 0:
#     sumRight += rightPart % 10
#     rightPart = rightPart // 10
# if sumLeft == sumRight:
#     print('yes')
# else:
#     print('no')


# a = 3
# b = 2
# c = 4
#
# if c % a == 0 or c % b == 0:
#     print("yes")
# else:
#     print("no")

# coins = [1, 0, 0, 1, 0, 0]
#
# # Введите ваше решение ниже
# count1 = 0
# count0 = 0
# for i in coins:
#     if i == 1:
#         count1 += 1
#     elif i == 0:
#         count0 += 1
# if count1 > count0:
#     print(count0)
# else:
#     print(count1)

# 15. Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза


# print("Enter quantity: ")
# quantity = int(input())
#
# size = [random.randint(2, 15) for i in range(quantity)]
# print(size)
# sizeMax = size[0]
# sizeMin = size[0]
# for i in size:
#     if i >= sizeMax:
#         sizeMax = i
#     elif i <= sizeMin:
#         sizeMin = i
# print(f"для себя: {sizeMax}, для тещи: {sizeMin}")


# Заданные значения суммы S и произведения P
# s = 12
# p = 27

# Находим все возможные пары чисел X и Y
# possible_pairs = []
# for x in range(1, min(s, p) + 1):
#     if p % x == 0:
#         y = p // x
#         if x + y == s and x <= y <= 1000:
#             possible_pairs.append((x, y))
#
# # Выводим результат
# for pair in possible_pairs:
#     print(pair[0], pair[1])
# possiblePairs = []


# s = 12
# p = 27
# for x in range(1, s):
#     if p % x == 0:
#         y = p // x
#         if x + y == s and x <= y <= 1000:
#             print(x, y)
# n = 16
# list_1 = [2 * i for i in range(n)]
# print(list_1)

# Заданное значение N
# n = 16
# maxPower = int(math.log(n, 2))
# list_1 = [2 ** i for i in range(maxPower + 1)]
# for i in list_1:
#     print(i)

# list_1 = [1, 2, 3, 4, 5, 3, 3]
# k = 3
#
# # Введите ваше решение ниже
# count = 0
# for i in list_1:
#     if i == k:
#         count += 1
# print(count)

#
# list_1 = [1, 2, 3, 4, 5, 100]
# k = 60
# minDiference = k
# minDiferenceItem = 0
# for i in range(len(list_1)):
#     if abs(list_1[i] - k) < minDiference:
#         minDiference = abs(list_1[i] - k)
#         minDiferenceItem = list_1[i]
# print(minDiferenceItem)
#
# k = 'car'
# sum = 0
#
# dictChars = {'AEIOULNSTRАВЕИНОРСТ': 1, 'DGДКЛМПУ': 2, 'BCMPБГЁЬЯ': 3, 'FHVWYЙЫ ': 4, 'KЖЗХЦЧ': 5, 'JXШЭЮ': 8,
#              'QZФЩЪ': 10}
# for i in k.upper():
#     for key in dictChars:
#         if i in key:
#             sum += dictChars[key]
# print(sum)


#
# sp = [-100, 12, "car", 4, False, 6, 8, True, "car", "car"]
# # sp.append('HI')
# # sp.insert(2, "three")
# sp.extend([1, 2, 3, 4, 5])
# print(sp)

#
# # for i, value in enumerate(sp):
# #     print(f"index = {i}, value = {value}")
# sp.pop(3)
# sp.remove("car")
# print(sp)
# Задача №17. Решение в группах Дан список чисел. Определите, сколько в нем встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4] Output: 6
# sp = [1, 1, 2, 0, -1, 3, 4, 4, 1, 3]
# unique_numbers = set(sp)
# count_unique = len(unique_numbers)
# print(count_unique)


# Задача №19. Решение в группах Дана последовательность из N целых чисел и число K. Необходимо сдвинуть
# всю последовательность (сдвиг - циклический) на K элементов вправо, K – положительное число.
# Input: [1, 2, 3, 4, 5] k = 2 Output: [4, 5, 1, 2, 3]
# sp = [1, 2, 3, 4, 5]
# k = int(input('Введите величину сдвига '))
# # print(sp[-k:] + sp[:-k])
# for _ in range(k):
#     sp.insert(0, sp.pop())
# print(sp)

# def count_workers(sp):
#     res = 0
#     for item in sp:
#         if isinstance(item, int):
#             res += item
#         else:
#             res += count_workers(item)
#     return res
#
#
# count_angola = 18
# count_new_york = [20, [10, 7]]
# count_chicago = 15
# count_usa = [count_new_york, count_chicago]
# count_all = [count_angola, count_usa]
# print(count_all)
# print(count_workers(count_all))

# Задача №31. Решение в группах Последовательностью Фибоначчи называется последовательность чисел a0 , a1 , ..., an , ...,
# где a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1). Требуется найти N-е число Фибоначчи Input: 7 Output: 21
# Число Фибоначи
# def fib(n):
#     if n in [1, 2]:
#         return 1
#     return fib(n - 1) + fib(n - 2)
#
#
# list_1 = []
# for i in range(1, 10):
#     list_1.append(fib(i))
# print(list_1)


# n = int(input("Введите число: "))

# def fib(n,a = 0,b = 1):
#     if n == 0:
#       return b
#     return fib(n-1,b,a + b)

# print(fib(n))
# Задача №33. Решение в группах Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные
# оценки на максимальные. Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на
# минимальные. Input: 5 -> 1 3 3 3 4 Output: 1 3 3 3 1

# def switch(li, max, count=0):
#     if count == len(li):
#         return
#     if li[count] == max:
#         li[count] = min(li)
#     count += 1
#     return switch(li, max, count)
#
#
# list_v = [1, 3, 5, 3, 4, 3, 1, 5]
# print(list_v)
# max = max(list_v)
# switch(list_v, max)
# print(list_v)

# for i in range(len(grades)):
#     if grades[i] == min_grade:
#         grades[i] = max_grade
#     elif grades[i] == max_grade:
#         grades[i] = min_grade

# print(grades)

# def fib(n):
#     if n == 1:
#         return 0
#     if n == 2:
#         return 1
#     return fib(n - 1) + fib(n - 2)
#
#
# print(fib(28))
# def palindrom(s):
#     if len(s) <= 1:
#         return True
#     if s[0] != s[-1]:
#         return False
#     return palindrom(s[1:-1])
# print(palindrom("шалаш"))
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# На вход подается 2 числа через пробел: n m
# n - кол-во элементов первого множества.
# m - кол-во элементов второго множества.
# Затем подаются элементы каждого множества через пробел в виде строки. ! Писать input() не надо
# var1 = '5 4'
# var2 = '1 3 5 7 9'
# var3 = '2 3 4 5'
# m1 = var1.intersection(var2)
# m2 = var1.intersection(var3)
# result = m1.intersection(m2)
# print(result)


# var1 = '5 4'
# var2 = '1 3 5 7 9'
# var3 = '2 3 4 5'
#
# n, m = map(int, var1.split())
# set1 = set(map(int, var2.split()))
# set2 = set(map(int, var3.split()))
#
# print(' '.join(map(str, sorted(set1.intersection(set2)))))
# arr = [555, 8000, 6, 4, 9, 2, 70, 30, 100000, 200000]
#
#
# def harvest(arr):
#     harvest_max1 = arr[-2] + arr[-1] + arr[0]
#     harvest_max2 = arr[0] + arr[1] + arr[-1]
#     if harvest_max1 > harvest_max2:
#         harvest_global_max = harvest_max1
#     elif harvest_max2 > harvest_max1:
#         harvest_global_max = harvest_max2
#
#     for i in range(len(arr) - 2):
#         harvest_sum_3 = arr[i] + arr[i + 1] + arr[i + 2]
#         if harvest_sum_3 > harvest_global_max:
#             harvest_global_max = harvest_sum_3
#
#     return harvest_global_max
#
#
# print(harvest(arr))
##################################################################
# def recursive_harvest(arr, index):
#     if index >= len(arr) - 1:
#         return 0
#
#     max1 = arr[-2] + arr[-1] + arr[0]
#
#     harvest_sum = max(max1, (arr[index - 1] + arr[index + 0] + arr[index + 1]))
#     return max(harvest_sum, recursive_harvest(arr, index + 1))
#
#
# arr = [2, 4, 10, 4, 2, 7]
# print(recursive_harvest(arr, 0))
# ##################################################


# arr = [9, 7, 3, 4, 2, 3, 7, 5]
# arr_count = list()
# for i in range(len(arr) - 1):
#     arr_count.append(arr[i - 1] + arr[i] + arr[i + 1])
# arr_count.append(arr[-2] + arr[-1] + arr[0])

# Вывод максимальной урожайности, которую может собрать собирающий модуль
# print(max(arr_count))
#
# def check_prime(n, i=2):
#     if n % i == 0:
#         return False
#
#     if i > n // 2:
#         return True
#     return check_prime(n, i + 1)
#
# n = int(input("Enter a number: "))
# print(check_prime(n))

#
# list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# min_number = 0
# max_number = 10
# for index, value in enumerate(list_1):
#     if min_number <= value <= max_number:
#         print(index)


# Заполните массив элементами арифметической прогрессии. Её первый элемент a1 , разность d и количество элементов n будет
# задано автоматически. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# list_1 = [i for i in range(n) if i == a1 + (n - 1) * d]
# a1 = 2
# d = 3
# n = 4
# list_1 = [a1 + i * d for i in range(n)]
# for i in range(len(list_1)):
#     print(list_1[i])

# for i in range(n):
#     print(a1 + i * d)

# print(sp := [randint(1, 10) for _ in range(10)])

# sp = [1, 23, 3, 4, 5, 6, 8, 9]
# print([item ** 2 for item in sp if item % 2])
# print([item ** 2 if item % 2 else 0 for item in sp])


##############################################################################
# sp = [1, 23, 3, 4, 5, 6, 8, 9]
# # print( [item for item in sp] )
# print([item ** 2 for item in sp if item % 2])  # количество элементов уменьшилось
# print([item ** 2 if item % 2 else 0 for item in sp])  # если надо одинаковое кол-во элементов
# # возвести в квадрат каждый нечетный элемент иначе вернуть ноль для каждого элемента в списке sp
# print({i: sp[i] for i in range(len(sp))})
# print({sp[i] for i in range(len(sp))})

###############################################################################

# Задача №39. Решение в группах Даны два массива чисел. Требуется вывести те элементы первого массива
# (в том порядке, в каком они идут в первом массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N чисел - элементы массива. Затем число M - количество элементов
# во втором массиве. Затем элементы второго


# list1 = [9, 7, 3, 4, 2, 3, 70, 5]
# list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# # checking_list = [el for el in list1 if el not in set(list2)]
# print([el for el in list1 if el not in set(list2)])
# Задача №41. Решение в группах Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве
# определит количество элементов, у которых два соседних и, при этом, оба соседних элемента меньше данного.
# Сначала вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив состоит из целых чисел.

# def find_local_max(i):
#     return list_3[i - 1] < list_3[i] > list_3[(i + 1) % len(list_3)]
#
#
# list_3 = [15, 6, 3, 12, 9, 0, 2, 20]
# res = len([list_3[i] for i in range(len(list_3)) if find_local_max(i)])
# print(f"лакальный макс: {res} ")


# Задача №43. Решение в группах Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается,
# что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать. Вводится список чисел.
# Все числа списка находятся на разных строках.  1 2 3 2 3  -> 2


# print(list_1 := [1, 2, 3, 2, 3, 3, 3, 5, 5])
# print(sum(list_2 := [list_1.count(i) // 2 for i in set(list_1)]))


# Задача №45. Решение в группах Два различных натуральных числа n и m называются дружественными, если сумма делителей
# числа n (включая 1, но исключая само n) равна числу m и наоборот. Например, 220 и 284 – дружественные числа. По данному
# числу k выведите все пары дружественных чисел, каждое из которых не превосходит k. Программа получает на вход одно
# натуральное число k, не превосходящее 105. Программа должна вывести  все пары дружественных чисел, каждое из которых
# не превосходит k. Пары необходимо выводить по одной в строке, разделяя пробелами. Каждая пара должна быть выведена
# только один раз (перестановка чисел новую пару не дает).


# def sum_divisors(n):
#     return sum([i for i in range(1, n) if n % i == 0])
#
#
# def find_friendly_numbers(k):
#     result = list()
#     for num in range(1, k + 1):
#         div_sum = sum_divisors(num)
#         if k >= div_sum != num and sum_divisors(div_sum) == num:
#             pair = (num, div_sum)
#             if pair not in result and (pair[1], pair[0]) not in result:
#                 result.append(pair)
#                 print(pair[0], pair[1])
#
#
# k = int(input("Введите натуральное число k: "))
# find_friendly_numbers(k)

# def sum_of_divisors(n):
#     return sum([i for i in range(1, n // 2 + 1) if n % i == 0])
#

# def friendly_nums(k):
#     list_friendly_nums = list()
#     for i in range(1, k + 1):
#         j = sum_of_divisors(i)
#         if sum_of_divisors(j) == i and j > i:
#             list_friendly_nums.append((i, j))
#     return list_friendly_nums
#
#
# k = int(input("Введите предел поиска: "))
# # print(*friendly_nums(k))
#
# print(*[(i, j) for i in range(1, k + 1) if sum_of_divisors(j := sum_of_divisors(i)) == i and j > i])


# def sum(a, b):
#     if b == 0:
#         return a
#
#     return sum(a + 1, b - 1)
#
#
# print(sum(10, 100))

# calc(lambda x, y: x + y, 4, 5)

#
# data = [1, 2, 3, 5, 8, 15, 23, 38]
# out = []
# for i in data:
#     if i % 2 == 0:
#         out.append((i, i ** 2))
# print(out)
# def select(f, col):
#     return [f(x) for x in col]
#
#
# def where(f, col):
#     return [x for x in col if f(x)]
#
#
# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = select(int, data)
# res = where(lambda x: x % 2 == 0, res)
# print(res)  # [2, 8, 38]
# res = list(select(lambda x: (x, x ** 2), res))


# Задача 30: Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: a n  = a1  + (n-1) * d.
# Каждое число вводится с новой строки.
# def arithmetic_progression(a1, n, d):
#     return [a1 + i * d for i in range(n)]
#
#
# a1 = int(input("Enter the first number a1: "))
# d = int(input("Enter the diff: d "))
# n = int(input("Enter the number of elements n:"))
#
# print(*map(str, (arithmetic_progression(a1, n, d))))


# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
# def find_index(arr, min_val, max_val):
#     index = [i for i, num in enumerate(arr) if min_val <= num <= max_val]
#     return index
#
#
# arr = [5, 10, 15, 20, 25, 30]
# min_val = 10
# max_val = 25
#
# result = find_index(arr, min_val, max_val)
# print("Индексы элементов в заданном диапазоне:")
# print(result)
#################################################
# Задача №47.

# def check_values(values):
#     transformed_values = list(map(lambda x: x, values))
#     return "ok" if values == transformed_values else "fail"
#
#
# values = [1, 23, 42, 'asdfg']
#
# print(check_values(values))


###################################################
# Планеты вращаются вокруг звезд по эллиптическим орбитам.
# Назовем самой далекой планетой ту, орбита которой имеет
# самую большую площадь. Напишите функцию
# find_farthest_orbit(list_of_orbits), которая среди списка орбит
# планет найдет ту, по которой вращается самая далекая
# планета. Круговые орбиты не учитывайте: вы знаете, что у
# вашей звезды таких планет нет, зато искусственные спутники
# были были запущены на круговые орбиты. Результатом
# функции должен быть кортеж, содержащий длины полуосей
# эллипса орбиты самой далекой планеты. Каждая орбита
# представляет из себя кортеж из пары чисел - полуосей ее
# эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b,
# где a и b - длины полуосей эллипса. При решении задачи
# используйте списочные выражения. Подсказка: проще всего
# будет найти эллипс в два шага: сначала вычислить самую
# большую площадь эллипса, а затем найти и сам эллипс,
# имеющий такую площадь. Гарантируется, что самая далекая
# планета ровно одна
# Вывод: 2.510 и этопланета № 2
# def find_farthest_orbit(list_of_orbits):
#     areas = [(math.pi * orbit[0] * orbit[1], orbit) for orbit in list_of_orbits if orbit[0] != orbit[1]]
#
#     return max(areas, key=lambda x: x[0])[1]
#
#
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(f*map(int, find_farthest_orbit(orbits)))


# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# result = filter(lambda x: x[0] != x[1], orbits)
#
# farthest_orbit = max(filter(lambda x: x[0] != x[1], orbits), key=lambda x: max(x))
#
# print(farthest_orbit)

# def find_farthest_orbit(orbits):
#     list_of_orbit_squares = list(map(lambda i: (i[0] != i[1]) * i[0] * i[1], orbits))
#     return orbits[list_of_orbit_squares.index(
#         max(list_of_orbit_squares))], f'\nНомер самой удалённой планеты: {list_of_orbit_squares.index(max(list_of_orbit_squares)) + 1}'
#
#
# orbits = [(1, 3), (7, 2), (6, 6), (4, 3), (2.5, 10)]
# print("Дуги орбиты самой дальней планеты:", *find_farthest_orbit(orbits))


# Задача №51. Решение в группах
# Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его
# характеристику


# def same_by(characteristic, objects):
#     if len(objects) <= 1:
#         return True
#     characteristic_values = [characteristic(obj) for obj in objects]
#     return all(value == characteristic_values[0] for value in characteristic_values)
#
#
# values = [1, 3, 5, 7]
# print("same" if same_by(lambda x: x % 2, values) else "different")

# def same_by_map(characteristic, objects):
#     return len(set(map(characteristic, objects))) in (0, 1)

#
# def same_by_all(characteristic, objects):
#     if not objects:
#         return True
#     first_characteristic = characteristic(objects[0])
#     return all(characteristic(obj) == first_characteristic for obj in objects)
#

# def same_by_filter(characteristic, objects):
#     different_objects = list(filter(characteristic, objects))
#     return len(different_objects) == len(objects) or not len(different_objects)
#
#
# values = [0, 1, 10, 6]  #
#
# if same_by_filter(lambda x: x % 2, values):
#     print('same')
# else:
#     print('different')
##########################################
# Напишите функцию print_operation_table(operation, num_rows, num_columns), которая принимает в качестве
# аргумента функцию, вычисляющую элемент по номеру строки и столбца. По умолчанию номер столбца и строки = 9.
#
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
#
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
#
# Если строк меньше двух, выдайте текст
# ОШИБКА! Размерности таблицы должны быть больше 2!.
#
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как,
# например, у операции умножения.
#
# Между элементами должен быть 1 пробел, в конце строки пробел не нужен.
# def print_operation_table(operation, num_rows=9, num_columns=9):
#     if num_rows < 2 or num_columns < 2:
#         print("ОШИБКА! Размерности таблицы должны быть больше 2!")
#         return
#
#     for i in range(1, num_rows + 1):
#         row_values = []
#         for j in range(1, num_columns + 1):
#             row_values.append(str(operation(i, j)))
#         print(' '.join(row_values))
#
#
# # Пример использования
# print_operation_table(lambda x, y: x * y, 5, 5)
# def check_rhythm(stroka):
#     phrases = stroka.split()
#
#     if len(phrases) <= 1:
#         return "Количество фраз должно быть больше одной!"
#
#     syllable_counts = []
#     for phrase in phrases:
#         syllable_count = sum(1 for char in phrase if char in 'аеёиоуыэюя')
#         syllable_counts.append(syllable_count)
#
#     if all(count == syllable_counts[0] for count in syllable_counts):
#         return "Парам пам-пам"
#     else:
#         return "Пам парам"
#
#
# stroka = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
# result = check_rhythm(stroka)
# print(result)
