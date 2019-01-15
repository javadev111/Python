# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

import os

count = 1
for i in os.listdir('.'):
    if os.path.isfile(i):
        pass
    else:
        print(f'{count}) {i}')
        count += 1
