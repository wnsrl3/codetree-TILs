n= int(input())

for i in range(0,n):
    print("* "*(n-i),end=" ")
    if i==5:
        break
    print()

for i in range(1,n):
        print("* "*(i+1))