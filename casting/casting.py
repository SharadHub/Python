# 1)Basic Comparison

# Write a program to check whether 25 is greater than 20, equal to 25, or less than 30. Print the results.
# Decision-Making
print(25 > 20)
print(25 == 25)  
print(25 < 30)  



# 2)Create a program that takes two numbers as input. If the first number is greater than the second, print "First number is larger". Otherwise, print "Second number is larger or equal".
# Using bool()
n = float(input("enter the number"))
m = float(input("enter the number"))
if(n > m):
    print(bool("First number is larger"))
elif(m > n):
    print(bool("Second number is larger"))
else:
    print(bool("Equal"))

# 3)Evaluate and print the Boolean value of:
# A non-empty string "Python".
# An empty string "".
# A number 0.
# A list [1, 2, 3].
# Truthy and Falsy Values
x = "cvb"
b = ""
z = 0
list = [1,2,3]
print(bool(x))
print(bool(b))
print(bool(z))
print(bool(list))

# 4)Write a function check_truthy(value) that takes a value and prints "True" if it’s truthy or "False" if it’s falsy. Test it with:
# 123, "Hello", [], {}, and None.
def truth(value):
    if bool(value):
        print(True)
    else:
        print(False)

truth(123)
truth("hello")
truth([])
truth({})
truth(None)

# Custom Objects
# 5)
# Create a class Custom with a __len__ method that always returns 0.
# Instantiate an object of this class and check its Boolean value using bool().
# Function Returning Boolean
class bishal:
    def __len__(self):
        return 0

object = bishal()
print(bool(object))

# 6)Write a function is_positive(num) that returns True if a number is positive and False otherwise. Test it with 10, -5, and 0.
def is_positive(num):
    return num> 0
print(is_positive(10))
print(is_positive(-5))
print(is_positive(0))


# Built-in Function: isinstance()
# 7)Write a program to check if the following variables are of type int using isinstance():
# x = 50, y = "Hello", z = [1, 2, 3]
x = 50
y = "Hello"
z = [1, 2, 3]
print(isinstance(x,int))
print(isinstance(y,int))
print(isinstance(z,int))