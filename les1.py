# coding: utf-8


import math

# easy
# 1
number = list(input('Введите целое число: '))
for i in number:
    print(i)


# 2
a = input('Введите значение переменной a: ')
b = input('Введите значение переменной b: ')
c = a
a = b
b = c
print('Теперь a=', a, ', а b=', b)


# 3
age = int(input('Введите ваш возраст: '))
if age >= 18:
    print('Доступ разрешен')
else:
    print('Извините, пользование данным ресурсом только с 18 лет')


# normal
# 1
number = list(input('Введите целое число: '))
max = int(number[0])
for i in number:
    if int(i) > max:
        max = int(i)
print('Максимальная цифра в числе: ', max)


# 2
a = input('Введите значение переменной a: ')
b = input('Введите значение переменной b: ')
a, b = b, a
print('Теперь a=', a, ', а b=', b)


# a = a + b
# b = a - b
# a = a - b


# 3
koef_a = int(input('Введите значение коэффициента a: '))
koef_b = int(input('Введите значение коэффициента b: '))
koef_c = int(input('Введите значение коэффициента c: '))
D = (koef_b ** 2) - (4 * koef_a * koef_c)
if D < 0:
    print('У данного уравнения нет корней среди действительных чисел!')
else:
    x1 = (- koef_b + math.sqrt(D)) / 2 * koef_a
    x2 = (- koef_b - math.sqrt(D)) / 2 * koef_a
    print('x1=', x1, ', x2=', x2)


# hard
# 1
number = int(input('Введите число: '))
if number == 1:
    print('Число простое')
else:
    counter = 0
    for i in range(number):
        a = i + 1
        if number % a == 0:
            counter += 1
    if counter == 2:
        print('Число простое')
    else:
        print('Число не простое')


# 2
# нумерация порядковых чисел Фибоначчи начинается с 1 (1-ое это 0, 2-ое - 1 и т.д.)
number = input('Введите порядковый номер числа Фибоначчи: ')
fibo_num = []
for i in range(number):
    if i == 0:
        fibo_num.append(i)
    elif i == 1:
        fibo_num.append(i)
    else:
        next_fibo_num = fibo_num[i - 1] + fibo_num[i - 2]
        fibo_num.append(next_fibo_num)
print(fibo_num[len(fibo_num - 1)])


# 3
n = int(input('Введите n: '))
m = int(input('Введите m :'))
aaa = 'AAA'
bbb = 'BBB'
sum = ''
for i in range(n):
    for j in range(m):
        if i % 2 == 0:
            sum += aaa + bbb
        else:
            sum += bbb + aaa
    print(sum)
    sum = ''
