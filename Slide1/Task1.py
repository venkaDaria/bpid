# Подсчет частоты встречаемости букв в тексте	
import re

# read file
file_name = input('Название файла? ')
with open(file_name) as file:
    data = file.read().replace('\n', '').lower()
data = re.findall('[^\W\d_]', data);

# frequency	
dict = { char: data.count(char) for char in data }

# write file
with open('st_' + file_name, 'w') as file:
    for char in sorted(dict, key = dict.get, reverse = True):
        file.write('{}: {}\n'.format(char, str(dict[char])))
        print(char, dict[char])
		
# write file (in 0.? format)
with open('freq_' + file_name, 'w') as file:
	for char in sorted(dict, key = dict.get, reverse = True):
		file.write('{}: {}\n'.format(char, str(dict[char] / len(data))))