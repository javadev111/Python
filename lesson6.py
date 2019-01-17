# coding utf-8
#
# Задача-1:
#
# Создать класс треугольник и реализовать в нем конструктор, методы для вычисления (не печати, нужен return) площади, периметра  и вывод значений сторон треугольника на экран.
# В конструкторе сделать проверку на возможность создания такого треугольника, если нет, то написать, что такой треугольник нельзя создать и сделать exit(1)


class Triangle:

    def __init__(self, a, b, c):
        self.side_a = a
        self.side_b = b
        self.side_c = c
        if self.side_a + self.side_b < self.side_c or self.side_a + self.side_c < self.side_b or self.side_c + self.side_b < self.side_a:
            print('Такой треугольник нельзя создать!')
            exit(1)

    def perimeter(self):
        return self.side_a + self.side_b + self.side_c

    def square(self):
        p = self.perimeter() / 2
        s = (p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c)) ** 0.5
        return s

    def print_sides(self):
        print(f'side a = {self.side_a}\nside b = {self.side_b}\nside c = {self.side_c}')


# Задание-2:
#
# Написать класс, который будет удобно использовать для работы с (на выбор что-нибудь одно) комплексными числами \ матрицами \ светофор \ микроволновка


class MicrowaveOven:

    def __init__(self, door: bool, volume: int, timer: int, control_panel: dict):
        self.door = door
        self.volume = volume
        self.timer = timer
        self.control_panel = control_panel

    def open_door(self):
        pass

    def close_door(self):
        pass

    def warming_up(self):
        pass

    def defrosting(self):
        pass

    def combo_mode(self):
        pass

    def start(self):
        pass

    def stop(self):
        pass
