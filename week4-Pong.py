# "Pong" mini-project

# This code runs under http://www.codeskulptor.org/ with python 2.7

#mini-project description:
# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_pos = [WIDTH/2,HEIGHT/2]
ball_vel = [0,0]


# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos[0] = WIDTH/2
    ball_pos[1] = HEIGHT/2
    #print direction

    if ((direction == "RIGHT") and (ball_vel[0] < 0)):
        ball_vel[0] = -ball_vel[0]



# define event handlers
def new_game():
    global ball_pos, paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints

    dir = "RIGHT"

    paddle1_pos = HEIGHT /2
    paddle2_pos = HEIGHT /2
    paddle1_vel = 0
    paddle2_vel = 0
    score1 = 0
    score2 = 0
    if (dir == "RIGHT"):
        ball_vel[0] = random.randrange(120, 240)/60
    else:
        ball_vel[0] = -random.randrange(120, 240)/60
    ball_vel[1] = -random.randrange(60, 180)/60

    #print "ball_vel0", ball_vel
    spawn_ball (dir)

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel


    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")

    # update ball
    ball_pos[0]  +=  ball_vel[0]
    ball_pos[1]  +=  ball_vel[1]

    # collide and reflect off of left hand side of canvas
    if ball_pos[0] <= BALL_RADIUS+PAD_WIDTH:
        ball_vel[0] = - ball_vel[0]

    # collide and reflect off of right hand side of canvas
    if ball_pos[0] >= WIDTH - BALL_RADIUS -PAD_WIDTH:
        ball_vel[0] = - ball_vel[0]

    # collide and reflect off of left hand side of canvas
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]

    # collide and reflect off of right hand side of canvas
    if ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]

    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "White", "White")




    # update paddle's vertical position, keep paddle on the screen
    if ((paddle1_pos + paddle1_vel) < HEIGHT-HALF_PAD_HEIGHT) and ((paddle1_pos + paddle1_vel) > HALF_PAD_HEIGHT):
        paddle1_pos += paddle1_vel

    if ((paddle2_pos + paddle2_vel) < HEIGHT-HALF_PAD_HEIGHT) and ((paddle2_pos + paddle2_vel) > HALF_PAD_HEIGHT):
        paddle2_pos += paddle2_vel

    # draw paddles
    canvas.draw_polygon([(0, paddle1_pos-HALF_PAD_HEIGHT), (0, paddle1_pos+HALF_PAD_HEIGHT), (PAD_WIDTH, paddle1_pos+HALF_PAD_HEIGHT), (PAD_WIDTH, paddle1_pos-HALF_PAD_HEIGHT)], 1, "white","white")
    canvas.draw_polygon([(WIDTH-PAD_WIDTH, paddle2_pos-HALF_PAD_HEIGHT), (WIDTH-PAD_WIDTH, paddle2_pos+HALF_PAD_HEIGHT), (WIDTH, paddle2_pos+HALF_PAD_HEIGHT), (WIDTH, paddle2_pos-HALF_PAD_HEIGHT)], 1, "white","white")


    # determine whether paddle and ball collide
    # collide and reflect off of left hand side of canvas
    if ball_pos[0] <= BALL_RADIUS+PAD_WIDTH:
        if ((ball_pos[1] < paddle1_pos-HALF_PAD_HEIGHT) or (ball_pos[1] > paddle1_pos+HALF_PAD_HEIGHT)):
            score2 += 1
            #print "score2", score2
            spawn_ball("RIGHT")
        else:
            ball_vel[0]= 1.1 * ball_vel[0]
            ball_vel[1] = 1.1 * ball_vel[1]
            #print "ball_vel_increacse, 2, ", ball_vel

    # collide and reflect off of right hand side of canvas
    if ball_pos[0] >= WIDTH - BALL_RADIUS -PAD_WIDTH:
        if ((ball_pos[1] < paddle2_pos-HALF_PAD_HEIGHT) or (ball_pos[1] > paddle2_pos+HALF_PAD_HEIGHT)):
            score1 += 1
            #print "score1", score1
            spawn_ball("LEFT")
        else:
            ball_vel[0]= 1.1 * ball_vel[0]
            ball_vel[1] = 1.1 * ball_vel[1]
            #print "ball_vel increase, 1, ", ball_vel
    #print "ball_vel the same", ball_vel

    # draw scores
    canvas.draw_text( str(score1), (WIDTH/2 - 100, 100), 50, 'White')
    canvas.draw_text( str(score2), (WIDTH/2 + 100, 100), 50, 'White')

def keydown(key):
    global paddle1_vel, paddle2_vel
    acc = 5
    if key==simplegui.KEY_MAP["W"]:
        paddle1_vel = -acc
    elif key==simplegui.KEY_MAP["S"]:
        paddle1_vel = acc
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel = acc
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel = -acc


def keyup(key):
    global paddle1_vel, paddle2_vel

    if key==simplegui.KEY_MAP["W"]:
        paddle1_vel = 0
    elif key==simplegui.KEY_MAP["S"]:
        paddle1_vel = 0
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel = 0
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel = 0

def button_handler():
    new_game()

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button('Restart', button_handler, 100)

# start frame
new_game()
frame.start()
