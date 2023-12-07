# A triangle can be classified based on the lengths of its sides as equilateral, isosceles or scalene. 
# All 3 sides of an equilateral triangle have the same length. An isosceles triangle has two sides that 
# are the same length, and a third side that is a different length. If all of the sides have different 
# lengths then the triangle is scalene. Write a program that reads the lengths of 3 sides of a triangle 
# from the user. Display a message indicating the type of the triangle.

# doing it with variable because we need the value to be stored and accessed for comparing 
side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))

if  side1 == side2 == side3:
    print("This triangle is equilateral.")
elif  side1 == side2 or side1 == side3 or side2 == side3:
    print("The triangle is isosceles.")
else:
    print("The triangle is scalene.")