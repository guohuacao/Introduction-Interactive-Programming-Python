
# Rock-paper-scissors-lizard-Spock

# This code runs under http://www.codeskulptor.org/ with python 2.7

#Mini-project description — Rock-paper-scissors-lizard-Spock

#Rock-paper-scissors is a hand game that is played by two people. The players count to three in unison and simultaneously "throw” one of three hand signals that correspond to rock, paper or scissors. The winner is determined by the rules:

#    Rock smashes scissors
#    Scissors cuts paper
#    Paper covers rock

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        return "Bad Name"


def number_to_name(number):
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        return "Bad Number"


###################################################
# Output to the console should have the form:
# rock
# Spock
# paper
# lizard
# scissors
import random

def rpsls(player_choice):
    print "player choose", player_choice

    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0, 4, 1)
    #print comp_number

    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)

    # print out the message for computer's choice
    print "computer choose", number_to_name(comp_number)

    diff = (name_to_number(player_choice) - comp_number) % 5

    if diff == 1:
        print player_choice, " wins!"
    elif diff == 2:
        print player_choice, " wins!"
    elif diff == 3:
        print number_to_name(comp_number), "wins!"
    elif diff == 4:
        print number_to_name(comp_number), "wins!"
    else:
        print "tie!"

    print "\n"




# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric
