# Шифр Цезаря (реализация)

# read file
file_name = input('Название файла? ')
with open(file_name) as file:
    data = file.read()	
count = int(input('Шаг сдвига: '))

# get new letters line
letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
while count < -len(letters):
    count += len(letters)
while count > len(letters):
    count -= len(letters)
newletters = letters[count:] + letters[:count]

# encode message
answer = ''
for char in data:
    newchar = char
    place = letters.find(char.lower())
    if place != -1:
        newchar = newletters[place]
        if char.isupper():
            newchar = newchar.upper()
    answer += newchar

# write file	
with open('enc_' + file_name, 'w') as file:
    file.write(answer)