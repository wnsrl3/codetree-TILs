n= int(input())
check=0
for i in range(1,n+1):
    if n%i==0:
        check=1
    else:
        check=0
        
if check==1:
    print("P")
else :
    print("C")