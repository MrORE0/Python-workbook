# Note  Frequency (Hz) 
# C4    261.63
# D4    293.66
# E4    329.63
# F4    349.23 
# G4    392.00 
# A4    440.00 
# B4    493.88
# Begin by writing a program that reads the name of a note from the user and displays the note’s frequency. 
# Your program should support all of the notes listed previously. Once you have your program working correctly 
# for the notes listed previously you should add support for all of the notes from C0 to C8. 
# While this could be done by adding many additional cases to your if statement, such a solution is cumbersome, 
# inelegant and unacceptable for the purposes of this exercise. Instead, you should exploit the relationship 
# between notes in adjacent octaves. In particular, the frequency of any note in octave n is half the frequency 
# of the corresponding note in octave n + 1. By using this relationship, you should be able to add support for 
# the additional notes without adding additional cases to your if statement.


# we can either make it as a bunch of if statements or a match case statements, or with a simple dictionary
usr_input = input('Please type a note: ')

notes = {'C4': 261.63, 'D4': 293.66, 'E4': 329.63, 'F4': 349.23, 'G4': 392.00, 'A4': 440.00, 'B4': 493.88 }

if usr_input[0] == 'C': #since a string is just a list of characters, we can treat it as such and use the [0] to get the first char from out input
    ZeroInProgression = 261.63 / (2**4) #treat it as a mathematical progression and use the formula to find the very first of it
    if int(usr_input[1]) > 0: #if the octave is 0 we already have the answer, otherwise we calculate
        for number in range(int(usr_input[1])): #every next octave is twice the previous one so we calculate
            ZeroInProgression *= 2
    print('%.2f' % (ZeroInProgression)) # we just format our output so it matches the others
elif usr_input in notes:
    print(notes[usr_input])
else: 
    print('Your input is was not recognized.')

