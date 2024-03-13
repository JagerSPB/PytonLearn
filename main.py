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


print("Enter quantity: ")
quantity = int(input())

size = [random.randint(1, 10) for i in range(quantity)]
print(size)
sizeMax = size[0]
sizeMin = size[0]
for i in size:
    if i >= sizeMax:
        sizeMax = i
    elif i <= sizeMin:
        sizeMin = i
print(f"Макс: {sizeMax}, Мин: {sizeMin}")
