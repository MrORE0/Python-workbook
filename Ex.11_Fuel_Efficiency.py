# In the United States, fuel efficiency for vehicles is normally expressed in miles-per- gallon (MPG). 
# In Canada, fuel efficiency is normally expressed in liters-per-hundred kilometers (L/100 km). 
# Use your research skills to determine how to convert from MPG to L/100 km. 
# Then create a program that reads a value from the user in American
# units and displays the equivalent fuel efficiency in Canadian units.

mpg = float(input("How many miles per gallon is your car spending: "))
lph = 235.215 / mpg
print(f"Your car spends {mpg:.2f} miles-per-gallon or {lph:.2f} liters-per-gallon.")