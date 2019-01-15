# И второй скрипт, удаляющий эти папки.

import os

for i in range(1, 10):
    if f'dir_{i}' in os.listdir('.'):
        os.rmdir(f'dir_{i}')
