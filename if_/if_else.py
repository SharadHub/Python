#1.Write a program that takes an integer input and prints whether the number is positive, negative, or zero.
"""number = int(input("Enter the integer number:"))

if(number < 0):
    print("It is negative number")
elif(number > 0):
    print("It is positive number")
else:
    print("It is zero")"""

# 2. Write a program to determine the grade of a student based on their marks:

# Marks ≥ 90: Grade A
# Marks ≥ 80: Grade B
# Marks ≥ 70: Grade C
# Marks < 70: Fail
"""
Marks = float(input("Enter the marks obtained:"))

if(Marks >= 90):
    print("Grade A")
elif(Marks >= 80):
    print("Grade B")
elif(Marks >= 70):
    print("Grade C")
else:
    print("fail")"""

# Short-Hand If...Else
#3. Write a one-liner to check if a number is even or odd and print the result.
"""num = float(input("enter the number:"))
if num % 2 == 0: print("it is even")"""

#4. Logical Operators
# Write a program to check if a number is positive, less than 100, and divisible by 3.
"""num = float(input("enter the number:"))

if(num > 0 and num < 100 and num %3 == 0):
    print("it is positive, less than 100 and divisible by 3")
"""
#5. Nested If
# Write a program to check if a given year is a leap year. Use nested if conditions
"""
year = int(input("Enter the year: "))

if year % 400 == 0:
    print("It is a leap year")
elif year % 100 == 0:
    print("It is not a leap year")
elif year % 4 == 0:
    print("It is a leap year")
else:
    print("It is not a leap year")

"""



#6. Membership Condition
# Write a program to check if the word "Python" exists in a sentence entered by the user.
"""
sentence = str(input("enter the sentence:"))

if('python' in sentence):
    print("yes, it is there")
else: 
    print("it is not there")
"""
#7. Complex Condition
#Write a program to calculate the largest of three numbers entered by the user using nested if statements.
"""
num1 = int(input("enter first number:"))
num2 = int(input("enter second number:"))
num3 = int(input("enter third number:"))

if(num1 > num2):
    if(num1 > num3):
        print("first number is the greatest")
    else:
        print("third number is the greatest")
elif not (num1 > num2):
    if(num2 >= num3):
        print("second number is the greastest")
    else:
        print("third number is the greastest")
"""
    
#8. The pass Statement
# Write a program that contains an empty if block but still runs without error
"""odd = 63
if odd > 0:
    pass"""