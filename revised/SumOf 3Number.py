number = int(input("Enter the 3 digits number:"))

a = number % 10

number =number // 10
b = number % 10

number = number // 10
c = number % 10

print(a+b+c)
