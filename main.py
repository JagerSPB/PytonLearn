import math
import random
import sys


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

# k = 'car'
# sum = 0
# dictChars = {'AEIOULNSTRАВЕИНОРСТ': 1, 'DGДКЛМПУ': 2, 'BCMPБГЁЬЯ': 3, 'FHVWYЙЫ ': 4, 'KЖЗХЦЧ': 5, 'JXШЭЮ': 8,
#              'QZФЩЪ': 10}
# for i in k.upper():
#     for key in dictChars:
#         if i in key:
#             sum += dictChars[key]
# print(sum)
# sp = [-100, 12, "car", 4, False, 6, 8, True, "car", "car"]
# # sp.append('HI')
# # sp.insert(2, "three")
# sp.extend([1, 2, 3, 4, 5])
# print(sp)
# #
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
# n = int(input("кол-во оценок "))
# list1 = [random.randint(1, 50) for i in range(n + 1)]


# grades = [5, 1, 3, 3, 3, 4]
# 
# min_grade = min(grades)
# max_grade = max(grades)
# 
# for i in range(len(grades)):
#     if grades[i] == min_grade:
#         grades[i] = max_grade
#     elif grades[i] == max_grade:
#         grades[i] = min_grade
# 
# print(grades)