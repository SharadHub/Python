
#print datatype of following data
a = "Python"
b = 42
c = 3.14
d = ["apple", "orange", "banana"]
e = {"name": "Alice", "age": 30}
f = {"apple", "banana", "cherry"}
g = frozenset({"apple", "banana", "cherry"})
h = True
i = b"Hello"
j = None
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))
print(type(i))
print(type(j))

#convert list to tuple
my_list = [1, 2, 3]
t = tuple(my_list)
print(t)

#convert string to integer and integer to float 
x = "12345"
x = int("12345")
print(x)
x = float(x)
print(x)

#convert set to frozenset
my_set = {"dog", "cat", "bird"}
fs = frozenset(my_set)
print(fs)


# Exercise 3: Experiment with Constructors
# Use the dict constructor to create a dictionary with keys "city" and "population", and values "Kathmandu" and 1000000.
x = dict([("city","Kathmandu"),("population","1000000")])
print(x)

# # Create a bytearray of size 10 and print it.
array = bytearray(10)
print(array)
