'''Даны две строки строчных латинских символов: строка J и строка S. Символы, входящие в строку J, — «драгоценности»,
входящие в строку S — «камни». Нужно определить, какое количество символов из S одновременно являются «драгоценностями».
Проще говоря, нужно проверить, какое количество символов из S входит в J.'''

J = set(input())
S = list(input())
all_numbers = 0
for i in J:
	for s in S:
		if i == s:
			all_numbers +=1
print(all_numbers)
