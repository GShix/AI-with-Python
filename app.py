# variable
import math
course = "Python Programming"

# function
print(len(course))
print(course[-1])

# slicing
print(course[0:6])  # Python
print(course[0:])  # Python Programming
print(course[:3])  # Pyt
print(course[:])  # Python Programming

# problem
# Using escaped quotes to include double quotes in the string
course2 = "Python \"Programming"
print(course2)

# Escape sequence
course3 = "Python\nProgramming"  # Using \n for a new line
print(course3)
course4 = "Python\tProgramming"  # Using \t for a tab space
print(course4)

# concatenation
first_name = "Dambar"
last_name = "Gharti"
full_name = first_name + " " + last_name
print(full_name)  # Dambar Gharti

# formatted string
full_name2 = F"{first_name} {last_name}"  # f and {2+2} can be used
print(full_name2)  # Dambar Gharti

# String Methods
course5 = "Python Programming"
course5.upper().lower().title()

# remove whitespace
course6 = "   Python Programming   "
print(course6.strip())  # removes whitespace from both sides
print(course6.lstrip())  # removes whitespace from the left side
print(course6.rstrip())  # removes whitespace from the right side

# finds the index of the first occurrence of the substring "gram"
print(course5.find("gram"))
course6.replace("p", "d")

# checks if the substring "pro" is in course6 and returns True or False
print("pro" in course6)
# checks if the substring "swift" is not in course6 and returns True or False
print("swift" not in course6)

# Numbers
x = 10
y = 3.1
z = 1+2j  # complex number

# operations
print(10 + 3)  # addition
print(10 - 3)  # subtraction
print(10 * 3)  # multiplication
print(10 / 3)  # division
print(10 // 3)  # floor division
print(10 % 3)  # modulus
print(10 ** 2)  # exponentiation

print(round(2.5))  # rounds to the nearest integer
print(abs(-2.5))  # returns the absolute value

print(math.ceil(3.2))  # rounds up to the nearest integer

#type conversion
x = 20 # converts to integer
print(type(x))  # <class 'int'>

a = input("X: ")
b = int(a) +2
print(f"a: {a}, b: {b}")