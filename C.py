last = None
new = int()
for _ in range(int(input())):
    new = int(input())
    if new !=last:
        print(new)
        last = new
