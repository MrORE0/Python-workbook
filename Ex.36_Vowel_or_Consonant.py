# In this exercise you will create a program that reads a letter of the alphabet from the user.
# If the user enters a, e, i, o or u then your program should display a message indicating 
# that the entered letter is a vowel. If the user enters y then your program should display 
# a message indicating that sometimes y is a vowel, and sometimes y is a consonant. 
# Otherwise your program should display a message indicating that the letter is a consonant.

vowels = ["a", "e", "i", "o", "u"]

letter = input("Please enter a letter: ")
if letter == "y":
    print("Sometimes 'y' can be a vowel and sometimes it can be a consonant.")
elif letter in vowels:
    print("The entered letter is a vowel.")
else :
    print("The entered letter is a consonant.")