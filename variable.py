
#1)Create a variable name and assign your name to it. Then, print it.

name= str(input("enter your name\n"))
print(f'{name}')

#2)Assign the value 5 to a variable x. Change its value to the string "hello" and print it
x = 5
x = 'hello'
print(x)


#3)Use the type() function to check the data types of the variables:
x = 10
y = "Python"
z = 3.14
print(type(x))
print(type(y))
print(type(z))

#4)Identify the errors in these variable names:

# 2name = "Alice"
# my-name = "Bob"
# class = "Python"
# 2name do not follow variable naming ruleas it is start from number
# my-name has that minus sign instead of underscore
# we cannot name class name as class = "Python"

#5)Rewrite the following variables using Snake Case:

My_Variable = 10
Total_Amount = 1000
print(My_Variable)
print(Total_Amount)

# 6)Assign the values "Apple", "Banana", and "Cherry" to the variables x, y, and z in one line. Print all the variables.
x,y,z = "Apple", "Banana", "Cherry"
print(x)
print(y)
print(z)


# 7)Assign the value "Orange" to three variables a, b, and c in one line and print them.
a = b = c = "Orange"
print(a)
print(b)
print(c)

#8)Unpack the following list into three variables x, y, and z, and print the variables:
fruits = ["apple", "banana", "cherry"]
x,y,z = fruits
print(x)
print(y)
print(z)

#9)Use the print() function to display the following:
"Python is fun"
x="python"
y="is"
z="fun"
print(x,y,z)
# Combine these variables into one sentence and print it:

lang = "Python"
adjective = "awesome"
print(lang,adjective)


# 10) Add two numbers a = 5 and b = 7, and print the result.
a = 5
b = 7
print(a+b)

# 11)Combine a string and a number in the print() function without causing an error:

x = 5
y = "years old"
print(x,y)

# 12) Create a global variable x = "great" and use it inside a function to print the message: "Python is great".
x = "great"

def display():
    print("Python is",x)

display()

# 13)Modify a global variable inside a function using the global keyword.
x = "great"

def display():
    x="fantastic"
    print("Python is",x)

display()
print("Python is",x)

# 14)Create a function where a local variable has the same name as a global variable. Print both the global and local values.
x = "great"

def display():
    x="fantastic"
    print("Python is",x)

display()
print("Python is",x)

# 15)Write a program that assigns a list of three favorite colors to three variables using unpacking and prints them as:
# My favorite colors are:
# 1. Red
# 2. Blue
# 3. Green
colors= ["Red", "Blue", "Green"]
a, b, c = colors
print("My favourite colors are:")
print(f"1. {a}")
print(f"2. {b}")
print(f"3. {c}")