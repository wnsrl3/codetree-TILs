import math
n= int(input())
prime=True
for i in range(2, int(math.sqrt(n)) + 1):
    if n%i==0:
        is_prime = False
        break
      
        
if prime and n > 1: 
    print("P")
else:
    print("C")