# coding: utf-8
import random
import string


# easy
# 1
food_list = ["яблоко", "банан", "киви", "арбуз"]
count = 1
for i in food_list:
    print(f'{count}. {i:>6}')
    count += 1


# 2
list1 = ['12', 123, 'fgdds', ['12', 123], 123.123]
list2 = ['12', ['12', 123], 123.123]
for i in list2:
    while i in list1:
        list1.remove(i)
print(list1)


# 3
list_number = [1, 34, 2345, 3456, 876, 456, 23, 3, 865]
list_number2 = []
for i in list_number:
    if i % 2 == 0:
        list_number2.append(i / 4)
    else:
        list_number2.append(i * 2)
print(list_number2)


# normal
# 1
list_number = [2, -5, 8, 9, -25, 25, 4]
list_number2 = []
for i in list_number:
    if i >= 0 and (i ** 0.5).is_integer():
        list_number2.append(i ** 0.5)
print(list_number2)


# 2
current_date = '19.12.2018.'
days = {
    '1': 'первое',
    '19': 'девятнадцатое'
}
months = {
    '11': 'ноября',
    '12': 'декабря'
}
date_list = current_date.split('.')
print(f'{days[date_list[0]]} {months[date_list[1]]} {date_list[2]} года.')


# 3
n = 10
list_numbers = []
for i in range(n):
    j = random.randint(-100, 100)
    list_numbers.append(j)
print(list_numbers)


# hard
# 1
user_text = input('Введите текст: ').lower()
for punct in string.punctuation:
    while punct in user_text:
        user_text = user_text.replace(punct, '')
text_list = user_text.split(' ')
print(f'В тексте {len(text_list)} слов')
text_list2 = ''.join(text_list)
count = 0
for i in range(97, 123):
    if chr(i) in text_list2:
        count += 1
print(f'В тексте {count} букв латинского алфавита')


# 2
text1 = input('Введите текст 1: ').lower()
text2 = input('Введите текст 2: ').lower()
for punct in string.punctuation:
    while punct in text1:
        text1 = text1.replace(punct, '')
    while punct in text2:
        text2 = text2.replace(punct, '')
text_list1 = text1.split(' ')
text_list2 = text2.split(' ')
set_1 = set(text_list1)
print(set_1.intersection(text_list2))


