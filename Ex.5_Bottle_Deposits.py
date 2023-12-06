# In many jurisdictions a small deposit is added to drink containers to encourage people to recycle them. 
# In one particular jurisdiction, drink containers holding one liter or less have a $0.10 deposit, and drink 
# containers holding more than one liter have a $0.25 deposit.
# Write a program that reads the number of containers of each size from the user.
# Your program should continue by computing and displaying the refund that will be received for returning 
# those containers. Format the output so that it includes a dollar sign and always displays exactly 
# two decimal places.

bottle = float(input("What bottles are you inserting(litres)?\n"))
small_bottles = 0
big_bottles = 0

while bottle != 0:
    if bottle <= 1:
        small_bottles += 1
    else:
        big_bottles +=1
    bottle = float(input(""))

print("Less than 1 litre: %d = %.2f$" % (small_bottles, small_bottles * 0.10))
print("More than 1 litre: %d = %.2f$" % (big_bottles, big_bottles * 0.25))
print("Total:%.2f" % ((small_bottles * 0.10) + (big_bottles * 0.25)))