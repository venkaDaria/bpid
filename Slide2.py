# Реализовать xor при помощи and, or, not
def xor(a, b):
    return (a & ~b) | (~a & b)

# Шифрование методом одноразового блокнота
letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

# input data
message = input('Открытый текст: ')
key = input('Ключ: ')

# encoding
answer = ''
for char, keychar in zip(message, key):
    try:
        value = xor(letters.index(char.lower()), \
                    letters.index(keychar.lower())) % len(letters)
        answer += letters[value]
    except ValueError:
        answer += char
        
# output data
print(answer)
