a, b = map(int, input().split())

if a % 2 != 0:
    a += 1

i = a
while i <= b:
    print(i, end=" ")
    i += 2