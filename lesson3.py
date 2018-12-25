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
        if function_object():
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


# hard
# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

def read_file(f):
    f_copy = f.read()
    while '  ' in f_copy:
        f_copy = f_copy.replace('  ', ' ')
    f_copy = f_copy.split('\n')
    read_list = []
    for i in f_copy:
        read_list.append(i.split(' '))
    return read_list


with open('data/workers.txt', 'r', encoding='utf-8') as f:
    workers_list = read_file(f)


with open("data/hours_of.txt", 'r', encoding='utf-8') as f1:
    hourse_of_list = read_file(f1)


wage_list = []
for i in range(1, len(workers_list)):

    salary = int(workers_list[i][2])
    hour_rate = int(workers_list[i][4])

    for j in range(1, len(hourse_of_list)):

        hourse_of = int(hourse_of_list[j][2])

        if hourse_of_list[j][0] == workers_list[i][0] and hourse_of_list[j][1] == workers_list[i][1]:

            wage = salary / hour_rate * hourse_of
            if hourse_of > hour_rate:
                wage = salary +  2 * salary / hour_rate * (hourse_of - hour_rate)

            wage_list.append([workers_list[i][0], workers_list[i][1], wage])
            break

print(wage_list)

# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))


with open("data/fruits.txt", 'r', encoding='utf-8') as f:
    f_copy = (f.read().split('\n\n'))

rus_alphabet_list = list(map(chr, range(ord('А'), ord('Я')+1)))
for i in rus_alphabet_list:
    for j in f_copy:
        if j[0] == i:
            file = open(f'data/fruits_{i}.txt', 'a', encoding='utf-8')
            file.write(f'{j}\n\n')
            file.close()
