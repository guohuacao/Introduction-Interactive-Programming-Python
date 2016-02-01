# "Guess the number" mini-project

# This code runs under http://www.codeskulptor.org/ with python 2.7

#mini-project description:
#Two player game, one person thinks of a secret number, the other peson trys to guess
#In this program, it will be user try to guess at input field, program try to decide
#"higher", "lower" or "correct"

# input will come from buttons and an input field
# all output for the game will be printed in the console


import simplegui
import random
import math


num_range = 100
remaining_guess = 7
# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global num_range
    global computer_guess
    global remaining_guess
    if (num_range == 100):
        remaining_guess = 7
    else:
        remaining_guess = 10
    print "\n"
    print "New game. Range is from 0 to ",num_range
    print "Number of remaining guess is ",remaining_guess
    computer_guess = random.randint(0, num_range)
    #print "computer gues was " ,computer_guess

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game
    global num_range
    global remaining_guess
    num_range = 100
    remaining_guess = 7
    new_game()


def range1000():
    # button that changes the range to [0,1000) and starts a new game
    global num_range
    global remaining_guess
    num_range = 1000
    remaining_guess = 10
    new_game()

def input_guess(guess):
    global num_range
    global computer_guess
    global remaining_guess
    print "guess was ", guess
    guess_int = int(guess)
    if (guess_int > num_range or guess_int < 0):
        print 'number is out of range'
    elif guess_int > computer_guess:
        print 'Lower!'
        remaining_guess -=1
        print "remaining guess is ",remaining_guess
    elif guess_int < computer_guess:
        print 'Higher!'
        remaining_guess -= 1
        print "remaining guess is ",remaining_guess
    else:
        print 'Correct!'
        new_game()

    if (remaining_guess==0):
        print "Number of remaining guesses is 0"
        print " You ran out of guesses. The number was ", computer_guess
        new_game()
    else:
        print "\n"


# create frame
f = simplegui.create_frame("guess number", 200, 200)

f.add_button("Range is [0, 100)", range100, 200)
f.add_button("Range is [0, 1000)", range1000, 200)
f.add_input("Enter a guess", input_guess, 200)


new_game()

# always remember to check your completed program against the grading rubric
