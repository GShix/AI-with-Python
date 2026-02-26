# variable
import math
course = "Python Programming"

# function
# print(len(course))
# print(course[-1])

# slicing
# print(course[0:6])  # Python
# print(course[0:])  # Python Programming
# print(course[:3])  # Pyt
# print(course[:])  # Python Programming

# problem
# Using escaped quotes to include double quotes in the string
course2 = "Python \"Programming"
# print(course2)

# Escape sequence
course3 = "Python\nProgramming"  # Using \n for a new line
# print(course3)
course4 = "Python\tProgramming"  # Using \t for a tab space
# print(course4)

# concatenation
first_name = "Dambar"
last_name = "Gharti"
full_name = first_name + " " + last_name
# print(full_name)  # Dambar Gharti

# formatted string
full_name2 = F"{first_name} {last_name}"  # f and {2+2} can be used
# print(full_name2)  # Dambar Gharti

# String Methods
course5 = "Python Programming"
course5.upper().lower().title()

# remove whitespace
course6 = "   Python Programming   "
# print(course6.strip())  # removes whitespace from both sides
# print(course6.lstrip())  # removes whitespace from the left side
# print(course6.rstrip())  # removes whitespace from the right side

# finds the index of the first occurrence of the substring "gram"
# print(course5.find("gram"))
course6.replace("p", "d")

# checks if the substring "pro" is in course6 and returns True or False
# print("pro" in course6)
# checks if the substring "swift" is not in course6 and returns True or False
# print("swift" not in course6)

# Numbers
x = 10
y = 3.1
z = 1+2j  # complex number

# operations
# print(10 + 3)  # addition
# print(10 - 3)  # subtraction
# print(10 * 3)  # multiplication
# print(10 / 3)  # division
# print(10 // 3)  # floor division
# print(10 % 3)  # modulus
# print(10 ** 2)  # exponentiation

# print(round(2.5))  # rounds to the nearest integer
# print(abs(-2.5))  # returns the absolute value

# print(math.ceil(3.2))  # rounds up to the nearest integer

# type conversion
x = 20  # converts to integer
# print(type(x))  # <class 'int'>

# a = input("X: ")
# b = int(a) +2
# print(f"a: {a}, b: {b}")

# Falsy values
# "", '', 0, 0.0, [], {}, (), None - in bool = Falses
fruit = "Apple"
# print(fruit[1:-2])

# comparison operator
# <,>,<=,>=,==(checks type),!=

# Numerical presentation of letter
ord("b")
ord("B")

# conditional statements
# temp = input("Tempreature:")
# tempreature = int(temp)
# if tempreature > 30:
#     print("It's hot")
#     print("Drink Water")
# elif tempreature > 20:
#     print("It's normal")
# else:
#     print("It's cold")
# print("Go ahead")

# Ternary operator
age = 2
# if age > 18:
#     message = "Eligible"
# else:
#     message = "Not eligible"
message = "Eligible" if age > 18 else "Not Eligible"
# print(message)

# logical operator: and or not - short circuit
# one item must be true in - or operator
# if one items flase in - and operator (doesn't execute)
high_income = False
good_credit = False
student = False

# if (high_income or good_credit) or not student:
#     print("Eligible")
# else:
#     print("Not Eligible")

# chaining comparison operators
# age should be between 18 and 65
age = 12
# if age >= 18 and age <65:
# if 18 <= age < 65:
#     print("Eligible")

# foor loops
# for number in range(3):
#     print("Attempt", number+1)
#     print("Attempt", number+1, (number + 1) * ".")

# for number in range(1, 4): #start from number 1 to 3
#     print("Attempt", number, number * ".")

# for number in range(1, 10, 2):
#     print("Attempt", number, number*".")

# for else loop - else block will be executed if the loop is not terminated by a break statement
successful = True
# for number in range(3):
#     print("Attempt", number+1)
#     if successful:
#         print("Successful")
#         break
# else:
#     print("Attempted 3 times and failed")

# Nested loops
for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")
