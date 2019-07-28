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
