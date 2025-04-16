# 1. Arithmetic Operators
# Write a program to calculate the area and perimeter of a rectangle. Use the +, *, and / operators.
"""
x = 15
y = 20 
area = x * y
perimeter = 2*(x + y)
print("Area of the rectangle is:",area)
print("Perimeter of the rectangle is:",perimeter)"""

# 2. Assignment Operators
# Write a program that starts with x = 10 and modifies its value using +=, -=, *=, /=, and **= operators. Print the value of x after each operation.
'''x = 10
x += 10
print(x)

x -= 10 
print(x)

x *= 10 
print(x)

x /= 10
print(x)

x **= 10
print(x)'''

# 3. Comparison Operators
# Write a program to compare two numbers entered by the user and print which one is larger, or if they are equal.
""" 
a = float(input("enter first number"))
b = float(input("enter second number"))
if(a>b):
    print(a,"is the large number")
else:
    print(b,"is the larger equal number")
"""
    

# 4. Logical Operators
# Check if a given number is positive, less than 100, and divisible by 5 using and, or, and not.
"""
g = int(input("enter the number"))

if(g > 0 and g < 100):
    print("it is positive number smaller than 100")
else:
    print("error")

if(g > 0 or g<100):
    print("it is greater tha 0 less than 100")

if(g % 5 == 0):
    print("it is divisible by 5")
else:
    print(not(g % 5 != 0))
    """
    


# 5. Identity Operators
# Create two lists and check if they are the same object using is and is not. Modify one list and observe if the change affects the other.
"""
color = ["blue","red","green"]
bibi = ["blue","red","green"]
diddy = color

print(diddy is color)
print(color is bibi)
print(color == bibi)
"""
# 6. Membership Operators
# Write a program to check if a particular word exists in a sentence entered by the user using in and not in.
"""
color = ["blue","red","green"]
print("red" in color)
print("red" not in color)"""


# 7. Bitwise Operators
# Perform bitwise operations (&, |, ^, ~) on two integers and print the results.
"""a = 1099
b = 2323

print(a & b) #AND
print(a | b) #OR
print(a ^ b) #XOR
print(~a)    #NOT
print(~b)    #NOT
"""

# 8. Operator Precedence
# Write a program to evaluate the expression 10 + 5 * 2 ** 2 - (5 + 3) and explain the order of operations.

print(10 + 5 * 2 ** 2 - (5 + 3))