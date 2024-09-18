def extract_numbers(s):
    return ''.join([char for char in s if char.isdigit()])


str1 = input().strip()
str2 = input().strip()


num1 = int(extract_numbers(str1))
num2 = int(extract_numbers(str2))


print(num1 + num2)