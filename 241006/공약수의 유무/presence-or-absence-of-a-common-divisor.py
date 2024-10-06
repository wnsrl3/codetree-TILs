a,b=map(int,input().split())
check=0
for n in range(a,(b+1)):
    if 1920%n==0 and 2880%n==0 :
        check=1
        break
    else :
        check=0

print(check)