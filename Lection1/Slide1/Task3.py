# Криптоанализ шифра Цезаря
import re

# read file
file_name = input('Название файла? ')
with open(file_name) as file:
    data = file.read()	

# read frequency (in 0.? format)
file_name_freq = input('Название файла частот? ')
with open(file_name_freq) as file:
    lines = file.readlines()

# get frequency
freq = {}
for line in lines:
    pair = line.split(': ')
    freq[pair[0]] = float(pair[1])

# get current frequency	
letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
newdata = [char for char in data.lower() if char in letters]	
current_freq = { char: newdata.count(char) / len(newdata) for char in newdata }
    
# check	frequency and get shift	
diff = 0.025
shiftes = [];
for current_freq_key, current_freq_value in current_freq.items():
    for freq_key, freq_value in freq.items():
        if current_freq_value >= freq_value - diff and current_freq_value <= freq_value + diff:
            try:
                shiftes.append(letters.index(current_freq_key) - letters.index(freq_key))
            except ValueError:
                pass
count = sorted(shiftes, key = shiftes.count,reverse = True)[0]

# get new letters line
count = -count
while count < -len(letters):
    count += len(letters)
while count > len(letters):
    count -= len(letters)
newletters = letters[count:] + letters[:count]

# decode
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
with open('dec_' + file_name, 'w') as file:
    file.write(answer)
