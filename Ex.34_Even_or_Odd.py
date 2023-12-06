# Write a program that reads an integer from the user. Then your program should
# display a message indicating whether the integer is even or odd.

number = int(input("Please enter an number(integer): "))
if number % 2 == 0:
    print("The number you've entered is even.")
else :
     print("The number you've entered is odd.")