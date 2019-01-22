# coding: utf-8
import random

# """
# == Лото ==
# Правила игры в лото.
# Игра ведется с помощью специальных карточек, на которых отмечены числа,
# и фишек (бочонков) с цифрами.
# Количество бочонков — 90 штук (с цифрами от 1 до 90).
# Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
# расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
# --------------------------
#     9 43 62          74 90
#  2    27    75 78    82
#    41 56 63     76      86
# --------------------------
# В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
# случайная карточка.
# Каждый ход выбирается один случайный бочонок и выводится на экран.
# Также выводятся карточка игрока и карточка компьютера.
# Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
# Если игрок выбрал "зачеркнуть":
#     Если цифра есть на карточке - она зачеркивается и игра продолжается.
#     Если цифры на карточке нет - игрок проигрывает и игра завершается.
# Если игрок выбрал "продолжить":
#     Если цифра есть на карточке - игрок проигрывает и игра завершается.
#     Если цифры на карточке нет - игра продолжается.
#
# Побеждает тот, кто первый закроет все числа на своей карточке.
# Пример одного хода:
# Новый бочонок: 70 (осталось 76)
# ------ Ваша карточка -----
#  6  7          49    57 58
#    14 26     -    78    85
# 23 33    38    48    71
# --------------------------
# -- Карточка компьютера ---
#  7 11     - 14    87
#       16 49    55 77    88
#    15 20     -       76  -
# --------------------------
# Зачеркнуть цифру? (y/n)
# Подсказка: каждый следующий случайный бочонок из мешка удобно получать
# с помощью функции-генератора.
# Подсказка: для работы с псевдослучайными числами удобно использовать
# модуль random: http://docs.python.org/3/library/random.html
# """


class Ticket:

    def __init__(self):

        self.ticket = [['  ' for i in range(9)] for j in range(3)]
        self.full_value_list = []

        for i in range(len(self.ticket)):

            value_list = []
            row_items = []

            while len(value_list) < 5:

                value = random.randint(1, 90)
                row_item = random.randint(0, 8)

                if (value in value_list) or (value in self.full_value_list) or (row_item in row_items):
                    continue
                else:
                    value_list.append(value)
                    row_items.append(row_item)
                    self.full_value_list.append(value)

            value_list.sort()
            row_items.sort()

            for j in range(len(row_items)):
                self.ticket[i][row_items[j]] = f'{value_list[j]:>2}'

    def print_ticket(self, player='comp'):
        if player == "user":
            print('------ Ваша карточка -----')
        else:
            print('--- Карточка компьютера --')
        for i in range(len(self.ticket)):
            for j in range(len(self.ticket[i])):
                print(f'{self.ticket[i][j]}', end=' ')
            print()
        print('-' * 26)

    def cross_out(self, number):
        if number in self.full_value_list:
            self.full_value_list.remove(number)
            for i in range(len(self.ticket)):
                for j in range(len(self.ticket[i])):
                    if f'{number:>2}' == self.ticket[i][j]:
                        self.ticket[i][j] = ' -'
        else:
            return 1


kegs = [i for i in range(1, 91)]


def get_keg():
    keg = random.randint(1, len(kegs))
    return kegs.pop(keg)


def has_winner():
    if user_ticket.full_value_list is None:
        return 1
    if comp_ticket.full_value_list is None:
        return 2


print("Приветствуем Вас в нашей лотерее!")

user_answer = input('Желаете получить карточку? (y/n): ')

user_ticket = Ticket()
comp_ticket = Ticket()

if user_answer == 'y':
    print('Вот Ваша карточка: ')
    user_ticket.print_ticket('user')
else:
    print('До скорых встреч!')
    exit(0)

user_answer = input('Нажмите \'y\' когда будете готовы начать игру! ')

if user_answer == 'y':

    print('Поехали!')
    while kegs:

        if has_winner() == 1:
            print("Поздравляю, Вы выйграли!")
            break
        elif has_winner() == 2:
            print("Выйграл компьютер!")
            break

        keg_num = get_keg()

        print('------------------------------------------------------------')
        print(f'Новый бочонок: {keg_num} (осталось {len(kegs)})')

        user_ticket.print_ticket('user')
        comp_ticket.print_ticket()

        comp_ticket.cross_out(keg_num)

        user_answer = input("Зачеркнуть цифру? (y/n): ")
        if user_answer == 'y':
            if user_ticket.cross_out(keg_num) == 1:
                print("Вы проиграли!")
                break
        else:
            if keg_num in user_ticket.full_value_list:
                print("Вы проиграли!")
                break



