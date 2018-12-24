# coding: utf-8


# easy
# 1

def my_round(number, ndigits):
    add_num = 5 / (10 ** ndigits)
    return (number + add_num) - (number + add_num) % (add_num * 2)


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# 2

def lucky_ticket(ticket_number):
    sum1 = 0
    sum2 = 0
    for i in range(5, 2, -1):
        sum1 +=  ticket_number // (10 ** i)
        ticket_number -= (ticket_number // (10 ** i)) * (10 ** i)
    for i in range(2, -1, -1):
        sum2 += ticket_number // (10 ** i)
        ticket_number -= (ticket_number // (10 ** i)) * (10 ** i)
    if sum1 == sum2:
        return 'Ваш билет счастливый!'
    else:
        return 'Ваш билет не счастливый!'


print(lucky_ticket(123006))
print(lucky_ticket(123212))
print(lucky_ticket(436751))


# normal
# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    fibo = []
    for i in range(m):
        if i == 0:
            fibo.append(i)
        elif i == 1:
            fibo.append(i)
        else:
            next_fibo = fibo[i - 1] + fibo[i - 2]
            fibo.append(next_fibo)
    return fibo[n - 1: m]

print(fibonacci(4, 20))


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    sort_list = []
    while origin_list:
        min_num = origin_list[0]
        for i in range(len(origin_list)):
            if origin_list[i] < min_num:
                min_num = origin_list[i]
        origin_list.remove(min_num)
        sort_list.append(min_num)
    print(sort_list)


sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])


# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def user_filter(function_object, iterable):
    f_iterable = []
    for i in iterable:
        if function_object() == True:
            f_iterable.append(i)
    return f_iterable


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.


A1 = [1, 1]
A2 = [3, 3]
A3 = [7, 3]
A4 = [5, 1]


def calc_coord(a, b):
    return [(a[0] + (b[0] - a[0]) / 2), (a[1] + (b[1] - a[1]) / 2)]


if calc_coord(A1, A3) == calc_coord(A2, A4):
    print('Это могут быть вершины параллелограмма.')
else:
    print('Это не вершины параллелограмма.')
