#1>Number Categorizer
#  Write a program to categorize a number entered by the user:

# If the number is divisible by 2 and 3, print "Divisible by both 2 and 3".
# If divisible only by 2, print "Divisible by 2".
# If divisible only by 3, print "Divisible by 3".
# Otherwise, print "Not divisible by 2 or 3".
"""
num = int(input("enter the number:"))

if(num % 2==0 and num %3==0):
    print("it is divisible by both")
elif(num % 2==0):
    print("divisible by 2 only")
elif(num % 3==0):
    print("divisible by 3")
else:
    print("not divisible by both")
"""
#2 Day Checker
# Ask the user to input a day (e.g., "Monday"), and print whether it's a weekday or weekend. Use a case-insensitive comparison.
"""
day = str(input("enter the day:"))

if(day == "saturday" or day == "sunday"):
    print("Weekend")
else:
    print("Weekday")
"""
# 3. Triangle Validator
# Write a program to check if three sides entered by the user can form a valid triangle:
# The sum of any two sides must be greater than the third side.
"""
side1 = float(input("enter first side"))
side2 = float(input("enter second side"))
side3 = float(input("enter third side"))

if(side1 < side2 + side3):
    if(side3 < side2 + side1):
        if(side2 < side1 + side3):
            print("it is triangle")
        else:
            print("it is not triangle")
    else:
        print("it is not triangle")
else:
        print("it is not triangle")
"""
#4. Grade Calculator
# Extend the grading program:

# Input marks for 5 subjects.
# Calculate the percentage and print the grade based on the following:
# ≥ 90%: Grade A
# ≥ 80%: Grade B
# ≥ 70%: Grade C
# < 70%: Fail
"""
obtained = 0

for i in range(5):
    marks = float(input(f"enter the marks {i+1}: "))
    obtained += marks

#pecentage calculated 
percent = (obtained / 500) * 100

#grade determination
if(percent >= 90):
    print("Grade A ")
elif(percent >= 80):
    print("Grade B")
elif(percent >=70):
    print("Grade C")
else:
    print("Fail")
"""
# 5. Nested Age Group Checker
# Write a program to classify people based on age:

# Child: Age < 12
# Teenager: 12 ≤ Age < 18
# Adult: 18 ≤ Age < 60
# Senior: Age ≥ 60
"""
age = int(input("enter the age:"))

if(age < 12):
    print("Child")
elif(12 <= age < 18):
    print("Teenager")
elif(18 <= age < 60):
    print("Adult")
else:
    print("Senior")
"""
# 6. Leap Year Enhancer
# Extend the leap year program:

# Input a range of years (start and end).
# Print all leap years within that range.
# Input: Start and end years
"""
start_year = int(input("enter the start year:"))
end_year = int(input("enter the end year:"))

if(start_year > end_year):
    print("invalid values")
else:
    print(f"leap years between {start_year} and {end_year} are:")

    for year in range(start_year , end_year + 1):
        if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print(year)
"""

#7. Write a program that calculates the discount based on the amount spent:

# If the amount is above $500, apply a 20% discount.
# If the amount is above $200 but ≤ $500, apply a 10% discount.
"""
expense = float(input("Enter the amount of money spent:"))

if(expense > 500):
    discount = (20/100) * expense
    print("the discount amount is", discount)
    print("the amount after discount is",expense-discount)
elif(200 < expense <= 500):
    discount = (10/100) * expense
    print("the discount amount is", discount)
    print("the amount after discount is",expense-discount)
else:
    print("No discount Scheme")
"""

#8. Quadratic Equation Roots
"""import math

a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))

# Calculate the discriminant
discriminant = b**2 - 4*a*c

if discriminant > 0:
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print(f"Two distinct real roots: {root1} and {root2}")
elif discriminant == 0:
    root = -b / (2*a)
    print(f"One real root: {root}")
else:
    real_part = -b / (2*a)
    imaginary_part = math.sqrt(-discriminant) / (2*a)
    print(f"Complex roots: {real_part} + {imaginary_part}i and {real_part} - {imaginary_part}i")
"""

#9. Character Classifier
# Write a program to classify a single character entered by the user:

# Vowel or Consonant if it's an alphabet.
# Digit if it's numeric.
# Special character otherwise.
"""
character = input("enter the character:")

if(character.isalpha()):
    if(character.lower() in "aeiou"):
        print(f"{character} is vowel")
    else:
        print(f"{character} is consonant")

elif(character.isdigit()):
    print(f"{character} is numeric")

else:
    print(f"{character} is a special character")
"""

# 10. Palindrome Checker
# Input a string and check if it is a palindrome (ignoring case and spaces).

"""
text = str(input("enter the text"))

norm_text = "".join(text.lower().split())

if(norm_text == norm_text[::-1]):
    print(f"{text} is a palindrome")
else:
    print((f"{text} is not a palindrome"))

"""


# 11. Number Pyramid
# Ask the user for a number, and build a pyramid up to that number.
"""row = 5

for i in range(1,row+1):

    for j in range(1,i+1):
        print(j, end="")
    print()

"""


# 12. Password Strength Checker
# Write a program to evaluate the strength of a password:

# Weak: Fewer than 8 characters or no uppercase letters.
# Moderate: 8+ characters but no special characters or numbers.
# Strong: 8+ characters with special characters and numbers.
"""
import re
password = input("enter the password")

if(len(password)< 8 and not any(char.isupper()) for char in password):
    print("Weak Password")
elif(len(password)>=8 and not re.search(r'[!@#$%^&*(),.?":{}|<>0-9]', password)):
    print("Moderate Password")
else:
    print("Strong Password")
   """

#13. FizzBuzz with Twist
# For a range of numbers from 1 to n (input by the user):

# Print "Fizz" if divisible by 3.
# Print "Buzz" if divisible by 5.
# Print "FizzBuzz" if divisible by both 3 and 5.
# Otherwise, print the number itself.
"""n = int(input("enter the range:")
          )
for num in range(1, n +1):
    if((num%5==0 and num%3==0)):
        print("FizzBuzz")
    elif(num%3==0):
        print("Fizz")
    elif(num % 5 == 0):
        print("Buzz")
    else:
        print(num)"""

# 14. BMI Calculator
# Write a program to calculate Body Mass Index (BMI) and classify the result:

# Underweight: BMI < 18.5
# Normal: 18.5 ≤ BMI < 25
# Overweight: 25 ≤ BMI < 30
# Obese: BMI ≥ 30
"""BMI = 0
weight = float(input("weight:"))
height = float(input("height"))

BMI = (weight / height)
if(BMI < 18.5):
    print("underweight")
elif(BMI< 25 and BMI >= 18.5):
    print("Normal")
elif( 25<= BMI < 30):
    print("Overweight")
elif(BMI >= 30):
    print("Obese")
"""

# 15.Odd/Even Digit Counter
# Write a program to count the number of odd and even digits in a given number.
"""number = input("enter the number")

odd = 0
even = 0

for digit in number:
    if digit.isdigit():
        if(int(digit)%2==0):
            even +=1
        else:
            odd +=1
print(f"Odd digits:{odd}, Even digits:{even}")"""










