# for i in range(1,3):
#  for j in range(2,3):
#   print(i,j)
print("hello")
                #tupples 
#are immutable and are  ordered collections of items created using () parentheses like list  they can duplicate items.
b_date  = ( 4, "DEC", 1998) 
print(b_date)
#calling  a certain item from the tupple

print("date", b_date[0])

sharon_birthday= ("sharon" , 1 ,"august" , 2000)
print ( "sharon's birthday = " ,sharon_birthday)
# count() function is used to calculate the number of occurencess of an item in a tuple


scores = (9,7,8,4,9,7,7)
print("# of 7: ", scores.count(7))
print("# of 9: ", scores.count(9))
print("# of 4: ", scores.count(4))
# the function len is used to count the number of items in a tuple
print(len(scores))
# the max function returns the maximum value in a collection
highest_score = max(scores)
# you can use tuples in any control flow structures suchb as if else statements
for score in scores:
    if score >7:
        print((score,": Passed"))
####
points =(12,14,9,10,9)
for point in points:
    if point >=14:
        print(point)

#tuple unpacking allows for assigning tuple items to variables . the values will be assigned in the order they appear in the tuple
# the number of variables should match the number of items in the tuple otherwise it will result to an error
sharon_birthday= ("sharon" , 1 ,"august" , 2000)
Name, Day,Month,Year =sharon_birthday
print(Name)
print(Day)
print(Month)
print(Year)
#  The * operator in tuple unpacking is used to gather multiple elements from a tuple into a list
scores =(98,96,91,88,64)
winner,*rest =scores
print(winner)
print(rest)

print ("start of collection of items")

# list, tuple, sets this are collection of items

#lists are  []
scoresL ={98,96,91,88,64}
#    modifiable
#    allow duplicates
#    are ordered
print ("List",scoresL)

# tuple are ()
scoreT =(98,96,91,88,64)
#     not modifiable
#     allow duplicates
#     are ordered
print("tuple",scoreT)
# sets are {}

scoresS ={98,96,91,88,64}

#    modifiable
#    doesn't allow duplicates
#    aren't ordered 

print("sets", scoresS)

                #dictionaries
# dictionaries are key value pairs created using {} curly braces/  they are collection types used to store data in key:value pairs,
# key value pairs are separated by commas 
#values can be of any data type,
#dictionaries can have duplicate values but not duplicate keys, values with duplicate keys will overwrite existing values
product ={
    "name":"pen",
    "color":"red",
    "price":79,
    "dark_mode":True,
    "points":[8,7,9]
}
print("Dictionary", product)
#to access values in dictionaries you need to use the keys
print(product["name"])
print(product["color"])
#you can also access values in a dictionary using the dot notation
info= product.get("name")
print("Using the dot notation",info)
print(info)
# you can get all the values and keys of a dictionary using the values() and keys() functions
print("Printing all values and keys of a dictionary")
info_keys=product.keys()
info_values=product.values()
print(info_keys, info_values)
#items() function returns all the key:value
infoo= product.items()
print("Printing all items of a dictionary")
print(infoo)

# you can loop through a dictionary using the for loop

for key in product:
    print(key, product[key])

#you can use keys to not only access values but also to modify them
user_dict ={
    "name":"sharon",
    "age":20
}
user_dict["age"] =21
print(user_dict["age"])

#The update() function updates the dictionaries with items from a given argument

user_dict.update({"age":22})

# the argument for the update function should be a dictionary and can accept multiple values 
user_dict.update({"age":22, "Surname": "Mutai"})

print(user_dict["age"])
print(user_dict.items())
# the pop() function removes the item with the specific key name. It accepts the key of the item you want to remove as an argument
user_dict.pop("Surname")
print(user_dict)
Car={
    "brand": "BMW",
    "Model": "I6",
    "color": "BLACK"
}

print(Car)


# error handling
#bugs are errors in a program that prevent it from running as expected, may not interrupt excecution

#Exception are specific errors that occur during a program excution and interupt its normal flow

#nameError is raised when an unknown variable is used
#syntaxError is raised when a syntax  mistake in the code is encountered
#IndexError is raised when you attempt to access an element of an iterable, ordered collection such as lists and tuples using an index that is outside its valid range
#TypeError is raised when a function is called on a value of an inapproriate type  len(5)
#valueError is raised when a function receives a value of the correct type but the value it self is inappropriate or unacceptable int("hello")

#There are three types of errors in python    

prices=[250,300,"240",400]      
try:
#block that may cause an exception
   total=sum(prices)
   print(total)
except TypeError:
#to perform if there is an exception
    print("invalid data type")
    
print("Happy Shopping")
###
color="green" 
try:
    print(color[5])               
except IndexError:
    print("index out of range")
print("Have a great day")
# the finally block is used to execute code regardless of whether an exception was raised or not
##
color ="grey"
try:
    print(hey)
except NameError:
    print("Check the variable name")
    
    ####you can have multiple except blocks to handle each possible exception specifically
    ### it's recommended output a definitive message for each type of handled exception

colors = ['red','blue','green']
try:
    print(colors[3])
except IndexError:
    print("Out of range")
except NameError:
    print("Variable is not defined")
print("great day")

## you can also choose not to specify the exception type which allows handling of any exception that may occur the downside is that the error message will be less specific
colors =["red","yellow","green"]
try:
    print(colors[10])
except:
    print("Error")
# you can use the finally statement to perform an operation after the try/except block whether an exception occured or not

prices =[559,879,"N/A",349]
try:
    print(sum(prices))
except TypeError:
    print("Check the Prices")
finally:
    print("Need help? Contact us")
##
####                    labdas
# lambda functions are small anonymous functions that are defined using the lambda keyword
greet = lambda name:"Welcome " + name

print(greet("Kelvin"))





##### decorators
# decorators are functions that modify/ enhance the functionality of other functions
# in python functions can be nested


def greet(name):
    print ("Hey", name)
    
    def welcome():
        print("welcome on board!")
        
#

# print (greet("Mutai"))                
greet("Mutai")            

# you can also return the rresult of the nested function directly from within the body of the parent function
def greet(name):
    print("Hey", name)
    
    def account():
        return "Your account is created"
    
    message = account()
    return message
print(greet("Kelvin K"))
#  decorators 

def greet():
    return "Welcome"
def uppercase(func):
    #wrapper function to keep the original function unchanged
    def wrapper():
        original_message = func()
        modified_result = original_message.upper()
        return modified_result
    return wrapper
greet_upper = uppercase(greet)
print(greet_upper())


# def greet():
#     return "Welcome"
# def uppercase(func):
#     #wrapper function to keep the original function unchanged
#     def wrapper():
#         original_message = func()
#         modified_result = original_message.upper()
#         return modified_result
# @uppercase
# def greet():
#     return "Welcome"
# # using the decorated function

# print(greet())

# You can easily check a variable’s data type using the type() function:
age= 25
print("Data type:",type(age))       # Outputs: <class 'int'>

# Control Flow - Making Decisions! 🧠

# Python can make decisions based on certain conditions, using if-else statements. This is called control flow—it helps us control how our code runs.


temperature = 30

if temperature > 25:
    print("It’s a hot day! ☀️")
else:
    print("It’s a cool day! ❄️")
    

# Control flow example for grading student marks
# This will ask the user for input and grade the student's performance

# Prompt the user for student marks
marks = int(input("Enter the student's marks (0-100): "))

# Grading system based on the marks
if marks > 70:
    print("Grade: Distinction 🏆")
elif marks >= 60:
    print("Grade: Credit 🎖️")
elif marks >= 50:
    print("Grade: Pass 👍")
else:
    print("Grade: Fail ❌")
    
# For Loop: Used for repeating tasks over a range.

# Repeats a block of code a fixed number of times.

# Print numbers 0 to 4
for i in range(5):
    print(i)
    
    
# While Loop: Runs as long as a condition is True.

# Repeats as long as a condition is true.


countdown = 5

while countdown > 0:
    print("Counting down:", countdown)
    countdown -= 1

print("Blast off! 🚀")

# Lists 📋
# Ordered collections that are mutable (changeable). Great for storing multiple items.

# A list is like a collection of items (e.g., a shopping list).



fruits = ["apple", "banana", "cherry"]

# Accessing elements
print(fruits[0])  # Outputs: apple

# Modifying an element
fruits[1] = "orange"
print(fruits)  # Outputs: ['apple', 'orange', 'cherry']

# Adding an element
fruits.append("grape")
print(fruits)  # Outputs: ['apple', 'orange', 'cherry', 'grape']

# Tuples 🔒
# Similar to lists but immutable (unchangeable).

# Tuples are like lists, but unchangeable. Once created, you can’t modify them.



coordinates = (10, 20)

# Accessing elements
print(coordinates[0])  # Outputs: 10

# Trying to modify a tuple will raise an error:
# coordinates[0] = 5  # Error! Tuples can't be modified.

# Sets 🔄
# Unordered collections of unique elements.

# A set is a collection of unique items (no duplicates allowed).


unique_numbers = {1, 2, 2, 3, 4}

print(unique_numbers)  # Outputs: {1, 2, 3, 4} (Notice that 2 is only included once)

# Dictionaries 📖
# Store key-value pairs. Think of it as a real-life dictionary, where you look up a word (key) to get its definition (value).

# A dictionary is like a phonebook—it stores key-value pairs.



student_info = {"name": "Charlie", 
                "age": 21, 
                "grade": "A"}

# Accessing a value by its key
print(student_info["name"])  # Outputs: Charlie

# Modifying a value
student_info["age"] = 22
print(student_info)  # Outputs: {'name': 'Charlie', 'age': 22, 'grade': 'A'}

#Functions are blocks of reusable code—they save you from repeating the same code over and over. Think of functions like superpowers you can call whenever you need them! 💪


# Defining a function
def greet(name):
    print("Hello, " + name + "! 👋")

# Calling the function
greet("Alice")  # Outputs: Hello, Alice! 👋
greet("Bob")    # Outputs: Hello, Bob! 👋