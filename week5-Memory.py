# "Memory" mini-project

# This code runs under http://www.codeskulptor.org/ with python 2.7

#mini-project description:
# Implementation of a Memory game

import simplegui
import random
Cards = range(0,8)
Cards.extend(range(0,8))
Card1_pos = -1
Card2_pos = -1
Turns = 0
state = 0

# helper function to initialize globals
def new_game():
    global Cards, Exposed, Turns
    random.shuffle(Cards);
    Exposed = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    Card1_pos = -1
    Card2_pos = -1
    Turns = 0
    state = 0


# define event handlers
def mouseclick(pos):
    global state, Exposed, Cards, Turns, Card1_pos, Card2_pos
    num = pos[0] / 50


    if state == 0:
        state = 1
        Exposed[num] = 1
        Card1_pos = num

    elif state == 1:
        if ( num == Card1_pos ):
            return
        state = 2
        Exposed[num] = 1
        Card2_pos = num
        Turns += 1
    else:
        state = 1
        if (( num == Card1_pos ) or ( num == Card2_pos )):
            return
        if (Cards[Card1_pos] != Cards[Card2_pos]):
            Exposed[Card1_pos] = 0
            Exposed[Card2_pos] = 0
        Exposed[num] = 1
        Card1_pos = num



# cards are logically 50x100 pixels in size
def draw(canvas):

    global Cards, Exposed, Turns
    index = 0
    for card in Cards:
        pos = index * 50 + 25;
        if (Exposed[index ]):
            canvas.draw_polygon([[pos-25, 0], [pos+25, 0], [pos+25, 100], [pos-25, 100]], 6, 'Green', 'Black')
            canvas.draw_text( str(card), (pos-12, 70), 64, 'White')
        else:
            canvas.draw_polygon([[pos-25, 0], [pos+25, 0], [pos+25, 100], [pos-25, 100]], 6, 'Green', 'Black')
        index +=1
    label.set_text("Turns = " + str(Turns))

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric
