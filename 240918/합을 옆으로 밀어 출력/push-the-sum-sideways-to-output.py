n = int(input())  

total_sum = 0
for _ in range(n):
    total_sum += int(input())

total_sum_str = str(total_sum)

shifted_result = total_sum_str[1:] + total_sum_str[0]

print(shifted_result)