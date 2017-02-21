1. Реализовать подсчёт статистик встречаемости букв.
Составить шаблоны для художественной и технической литературы,
молитв.
	source:
	Slide1/Task1.py
	
	input:
	text1.txt (художественная литература)
	text2.txt (техническая литература)
	text3.txt (молитва)

	output:
	st_text1.txt (количество)
	freq_text1.txt (десятичная дробь)
	st_text2.txt
	freq_text2.txt		
	st_text3.txt
	freq_text3.txt

2. Реализовать шифр Цезаря.
	source:
	Slide1/Task2.py	

	input:
	text1.txt
	text2.txt 
	text3.txt	

	output:
	enc_text1.txt
	enc_text2.txt 
	enc_text3.txt

3. Реализовать подсчёт статистик криптограмм, полученных 
методом Цезаря. Автоматизировать криптоанализ таких шифрограмм.
	source:	
	Slide1/Task3.py	

	input:
	enc_text1.txt
	enc_text2.txt 
	enc_text3.txt
	freq.txt (файл частот)	

	output:
	dec_enc_text1.txt
	dec_enc_text2.txt 
	dec_enc_text3.txt

4. Реализовать шифрование методом одноразовый блокнот.
	source:
	Slide2.py

	input: сообщение и ключ	

	Для абсолютной криптографической стойкости ключ 
	должен обладать тремя критически важными свойствами:
	1) иметь случайное равномерное распределение;
	2) совпадать по размеру с заданным открытым текстом;
	3) применяться только один раз.
	
5. Реализовать XOR при помощи and, or, not
	source:
	Slide2.py
	______________________________
	def xor(a, b):
   		return (a & ~b) | (~a & b)

_____________________________________________
Язык реализации: Python (Python 3.x)