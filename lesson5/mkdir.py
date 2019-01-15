#EASY

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.



import os

cur_dir_path = os.getcwd()

for i in range(1, 10):
    dir_path = os.path.join(cur_dir_path, f'dir_{i}')
    os.mkdir(dir_path)


