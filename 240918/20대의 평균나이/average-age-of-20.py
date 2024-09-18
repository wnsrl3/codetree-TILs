ages = []

while True:
    age = int(input())  
    if age < 20 or age >= 30:  
        break
    ages.append(age) 


average = sum(ages) / len(ages)  
print(f"{average:.2f}")