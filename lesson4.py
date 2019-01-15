# coding: utf-8

import random
#
# # EASY
# # Все задачи текущего блока решите с помощью генераторов списков!
#
# # Задание-1:
# # Дан список, заполненный произвольными целыми числами.
# # Получить новый список, элементы которого будут
# # квадратами элементов исходного списка
# # [1, 2, 4, 0] --> [1, 4, 16, 0]
#
# list_num = [1, 2, 4, 0]
# print([i ** 2 for i in list_num])
#
# # Задание-2:
# # Даны два списка фруктов.
# # Получить список фруктов, присутствующих в обоих исходных списках.
#
# fruits_list1 = ['яблоко', 'банан', 'мандарин', 'груша', 'киви']
# fruits_list2 = ['яблоко', 'груша', 'апельсин', 'киви', 'ананас']
# print([i for i in fruits_list1 if i in fruits_list2])
#
# # Задание-3:
# # Дан список, заполненный произвольными числами.
# # Получить список из элементов исходного, удовлетворяющих следующим условиям:
# # + Элемент кратен 3
# # + Элемент положительный
# # + Элемент не кратен 4
#
# number_list = [1, 4, 9, 12, -6, 6]
# print([i for i in number_list if i % 3 == 0 and i > 0 and i % 4 != 0])
#
#
# #NORMAL
# # Задание-1:
# # Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# # произвольными целыми цифрами, в результате в файле должно быть
# # 2500-значное произвольное число.
# # Найдите и выведите самую длинную последовательность одинаковых цифр
# # в вышезаполненном файле.
#
# with open('data\list2500numbers.txt', 'w', encoding='utf-8') as f:
#     f.write(''.join(str(random.randint(0, 9)) for i in range(2500)))
#
# with open('data\list2500numbers.txt', 'r', encoding='utf-8') as f1:
#     read_num = f1.read()
#
# ident_num = read_num[0]
# ident_num_value = 0
# count = 0
# max_count = 0
#
# for i in read_num:
#     if i == ident_num:
#         count += 1
#         if count > max_count:
#             max_count = count
#             ident_num_value = i
#     else:
#         ident_num = i
#         count = 0
# print(f'{ident_num_value}' * max_count)
#
# # Задание-2
# # Сформировать квадратную матрицу, в каждой строке которой находится ровно один ноль на случайном месте, остальные элементы тоже рандомные. Пользователь вводит размер
#
#
# matr_size = int(input('Введите размер матрицы: '))
# matr = [[random.randint(0, 9) for i in range(matr_size)] for j in range(matr_size)]
# count = 0
#
# for i in range(matr_size):
#     for j in range(matr_size):
#         if matr[i][j] == 0:
#             count += 1
#             null_num = j
#     if count == 0:
#         matr[i][random.randint(0, matr_size - 1)] = 0
#     elif count > 1:
#         matr[i][null_num] = random.randint(0, matr_size - 1)
#     count = 0
#     print(matr[i])


#HARD

# Задание-1
# Куб состоит из n^3 прозрачных и непрозрачных элементарных кубиков. Имеется ли хотя бы один просвет по каждому из трех измерений?
# Если это так, вывести координаты каждого просвета. Куб задается трехмерной матрицей из 0 и 1.

kub_size = int(input('Введите размер куба: '))
kub = [[[random.randint(0, 1) for i in range(kub_size)] for j in range(kub_size)] for z in range(kub_size)]
print(kub)

count = 0
for i in range(kub_size):
    for j in range(kub_size):
        for z in range(kub_size):
            if kub[z][j][i] == 0:
                count += 1
                if count == kub_size:
                    koord_i = z
                    koord_j = j
                    koord_z = i
            else:
                count = 0
                break
        if count == kub_size:
            print(f'kub[{koord_i}][{koord_j}][{koord_z}], kub[{koord_i - 1}][{koord_j}][{koord_z}], kub[{koord_i - 2}][{koord_j}][{koord_z}]')
            count = 0

sum_z = 0
for i in range(kub_size):
    for j in range(kub_size):
        for z in range(kub_size):
            sum_z += kub[i][j][z]
        if sum_z == 0:
            koord_i = i
            koord_j = j
            koord_z = z
            print(f'kub[{koord_i}][{koord_j}][{koord_z}], kub[{koord_i - 1}][{koord_j}][{koord_z}], kub[{koord_i - 2}][{koord_j}][{koord_z}]')
# Задание-2
# Дан pwd.txt с логинами и паролями. Найдите топ10 самых популярных паролей.
#

# Задание-3
# Пользователь вводит положительное целое число больше 1
# Нужно создать квадратную матрицу этого размера и по спирали заполнить её числами

# 5
#  1  2  3  4 5
# 16 17 18 19 6
# 15 24 25 20 7
# 14 23 22 21 8
# 13 12 11 10 9

# 3
# 1 2 3
# 8 9 4
# 7 6 5
