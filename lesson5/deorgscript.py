# HARD

# Задание-1
#
# Написать программу для распаковки файлов в корневую из всех папок с расширениями (код взять с урока) и папки удалить

import os
import sys

dir_path = input("Input path to dir: ")

if "win32" == sys.platform:
    dir_path = dir_path.replace("/", "\\")
else:
    dir_path = dir_path.replace("\\", "/")

list_dir = os.listdir(dir_path)

for current_dir in list_dir:
    if not os.path.isfile(current_dir):
        if current_dir.startswith('.'):
            for file in os.listdir(os.path.join(dir_path, current_dir)):
                os.rename(os.path.join(dir_path, current_dir, file), os.path.join(dir_path, file))

delete_num = []
for i in range(len(list_dir)):
        if list_dir[i].startswith('.') and not os.path.isfile(i):
            delete_num.append(i)

for i in delete_num:
    file_path = os.path.join(dir_path, list_dir[i])
    os.rmdir(file_path)
