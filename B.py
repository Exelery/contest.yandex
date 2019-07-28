'''Требуется найти в бинарном векторе самую длинную последовательность единиц и вывести её длину.
Желательно получить решение, работающее за линейное время и при этом проходящее по входному массиву только один раз.'''

n = int(input())
numbers = []
for _ in range(n):
	numbers.append(int(input()))
count = 0
best = 0
last = None
for i in numbers:
    if i == 1 and i != last:
        count = 1
        if count > best:
            best = count
    elif i == 1 and (i == last or last == None):
        count += 1
        if count > best:
            best = count
    else:
        count = 0
    last = i
print(best)
