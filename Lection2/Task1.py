# Энтропия. Для анализа взять тексты (2000-3000 знаков) 
# на русском, украинском и английском языках. 
# Оценить вероятность появления битов 0 или 1 в каждой позиции символа.

import re
import math

# read file
file_name = input('Название файла? ')
with open(file_name) as file:
    data = file.read().replace('\n', '').lower()
data = re.findall('[^\W\d_]', data);

# char to binary string
bytes = { char: bin(ord(char))[2:] for char in data }
bytes = { char: '0' * (16 - len(bytes[char])) + bytes[char] for char in bytes }

# probability and entropy -> write file
ent = 0
with open('ent_' + file_name, 'w') as file:
    for i in range(16):
        p = 0
        for key, value in bytes.items():
            p += 1 if value[i] == '1' else 0
        p /= len(bytes)
        file.write('p({}): {}\n'.format(i + 1, p))
        ent += 0 if p == 0 else p * math.log(p, 2)
    file.write('ent: {}\n'.format(-ent))
