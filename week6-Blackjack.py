# "Blackjack" mini-project

# This code runs under http://www.codeskulptor.org/ with python 2.7

#mini-project description:
# Implementation of classic blackjack game

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")

# initialize some useful global variables
In_play = False
Outcome = ""
Score = 0
Msg = "New Deal?"

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank),
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)

    def draw_back(self, canvas, pos):
        card_loc = (CARD_CENTER[0],CARD_CENTER[1])
        canvas.draw_image(card_back, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)

# define hand class
class Hand:
    def __init__(self):
        self.hand = []
        pass	# create Hand object

    def __str__(self):
        str = "Hands contains "
        for card in self.hand:
            str += card.__str__()
            str += " "
        return str


    def add_card(self, card):
        self.hand.append(card)

    def get_value(self):
        value = 0
        numA = 0
        for card in self.hand:
            if (card.rank != 'A'):
                value += VALUES[card.rank]
            elif numA:
                value += 1
            else:
                numA = 1
                value += 1
                if (value <= 11):
                    value +=10
        if ((value > 21) and (numA >= 1)):
            value -= 10
        return value

    def draw(self, canvas, pos):
        pass	# draw a hand on the canvas, use the draw method for cards


# define deck class
class Deck:
    def __init__(self):
        self.cards = []
        for suit in SUITS:
            for rank in RANKS:
                card = Card(suit, rank)
                self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()

    def __str__(self):
        str = " "
        for card in self.cards:
            str += card.__str__()
            str += " "
        return str



#define event handlers for buttons
def deal():
    global Outcome, In_play, Msg, Score

    global Deckcard, Dealer, Player

    if (In_play):
        Score -= 1
        Msg = "Can't deal right now!"
        Outcome = "Dealer Wins!"
        In_play = 0
        return

    Msg = "New Deal?"
    Outcome = ""

    Deckcard = Deck()
    Deckcard.shuffle()
    Dealer = Hand()
    Player = Hand()

    #display dealer cards
    Dealer.add_card(Deckcard.cards.pop())
    print "Dealer's first card is ", Dealer.hand[0].rank
    Dealer.add_card(Deckcard.cards.pop())

    #player cards
    Player.add_card(Deckcard.cards.pop())
    Player.add_card(Deckcard.cards.pop())

    In_play = True

def hit():
    global Outcome, In_play, Msg, Dealer, Player, Score

    if (In_play == False):
        return
    Player.add_card(Deckcard.cards.pop())
    val = Player.get_value()
    #print str(val)
    if (val > 21):
        Msg = "You have busted"
        In_play = False
        Score -= 1



    # if the hand is in play, hit the player

    # if busted, assign a message to outcome, update in_play and score

def stand():
    global Outcome, In_play, Msg, Dealer, Player, Score

    if (In_play == False):
        return
    Msg = "Stand"
    pval = Player.get_value()
    while (Dealer.get_value() < 18):
        Dealer.add_card(Deckcard.cards.pop())
        dval = Dealer.get_value()
        #print str(dval) + "  "

        if (dval > 21):
            Score += 1
            Outcome = "Dealer Loose!"
            In_play = 0
            return
        if (Dealer.get_value() > pval ):
            Score -= 1
            Outcome = "Dealer Win!"
            In_play = 0
               #Msg ?
            return

    dval = Dealer.get_value()
    #print str(dval) + "  "
    if (dval > 21):
        Score += 1
        Outcome = "Dealer Loose!"
        In_play = 0

    if (dval > pval ):
        Score -= 1
        Outcome = "Dealer Win!"
        In_play = 0
    else:
        Score += 1
        Outcome = "Dealer Loose!"
        In_play = 0
    return

    # assign a message to outcome, update in_play and score

# draw handler
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    global Dealer, Player, Outcome, Score, Msg

    pos = [0, 170]
    i = 0
    for card in Dealer.hand:
        pos[0] += 100
        if (i==0):
            card.draw_back(canvas, pos)
            i +=1
        else:
            card.draw(canvas, pos)

    pos = [0,350]
    for card in Player.hand:
        pos[0] += 100
        card.draw(canvas, pos)

    canvas.draw_text('Blackjack', (120, 100), 36, 'Aqua')
    canvas.draw_text('Dealer', (100, 150), 24, 'Black')
    canvas.draw_text(Outcome, (250, 150), 24, 'Black')

    canvas.draw_text('Player', (100, 330), 24, 'Black')
    canvas.draw_text( Msg, (250, 330), 24, 'Black')
    canvas.draw_text('Score  '+ str(Score), (400, 100), 24, 'Black')



# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
Deckcard = Deck()
Dealer = Hand()
Player = Hand()
deal()
frame.start()


# remember to review the gradic rubric
