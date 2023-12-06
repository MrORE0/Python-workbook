# The length of a month varies from 28 to 31 days. In this exercise you will create a program that
# reads the name of a month from the user as a string. Then your program should display the number 
# of days in that month. Display “28 or 29 days” for February so that leap years are addressed.

months = {"January": 31, "February": "28 or 29", "March": 31, "April": 30, "May": 31, "June": 30, "July": 31, "August": 31, "September": 30, "October": 31, "November":30, "December": 31}
user_input = input("Please enter a month: ")

# adding this so we can always check the dictionary regarding of the way the user entered the month 
# (march, March, MARCH)
user_input = user_input.capitalize() 
if user_input in months:
    print(f"The month you've entered has {months[user_input]} days")
else:
    print("Please enter a valid month.")