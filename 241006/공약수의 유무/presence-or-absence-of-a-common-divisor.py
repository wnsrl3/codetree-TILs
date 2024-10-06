a,b=map(int,input().split())

for n in range(a,(b+1)):
    if 1920%n==0 and 2880%n==0 :
        print(1)
        break
    else :
        print(0)