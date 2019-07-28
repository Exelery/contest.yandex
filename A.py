J = set(input())
S = list(input())
all_numbers = 0
for i in J:
	for s in S:
		if i == s:
			all_numbers +=1
print(all_numbers)
