# Create a program that reads two integers, a and b, from the user. Your program should
# compute and display:
# • The sum of a and b
# • The difference when b is subtracted from a 
# • The product of a and b
# • The quotient when a is divided by b
# • The remainder when a is divided by b
# • The result of lg(a)
# • The result of a^b

import math

a = int(input("Integer a = "))
b = int(input("Integer b = "))


print("sum =",a + b)
print("difference =",a - b)
print("product =",a * b)
# idk if they want them as integers or floats
print("quotient =", a // b)
print("remainder =", a % b)
print("lg(a) =", math.log10(a))
print("power(a,b) =", math.pow(a,b))