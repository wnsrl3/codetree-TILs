n = int(input())  
c = 0  
i = 1

while n > 1:  
    n = n // i  
    i += 1  
    c =c+ 1  

print(c)