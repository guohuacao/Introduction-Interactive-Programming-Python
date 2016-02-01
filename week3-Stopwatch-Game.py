# "Stopwatch: The Game" mini-project

# This code runs under http://www.codeskulptor.org/ with python 2.7

#mini-project description:
#implement a stop watch and to see if you can stop the watch on 1/10th seconds

# CodeSkulptor runs in Chrome 18+, Firefox 11+, and Safari 6+.
# Some features may work in other browsers, but do not expect
# full functionality.  It does NOT run in Internet Explorer.


import simplegui
# define global variables

interval = 100
Time = 0
Score = "0/0"
Timer_status = False

Num_Scores = 0
Num_Games = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    if (Time == 0):
        return "0:00.0"
    else:
        Min = Time / 600
        if ( Min > 0 ):
            min_str = str ( Min)
        else:
            min_str = "0"


        Sec = Time / 10
        Sec = Sec % 60
        if (Sec < 10):
            sec_str = "0" + str(Sec)
        else:
            sec_str = str(Sec)
        Milisec = Time  % 10
        # print Milisec
        milisec_str = str (Milisec)

        return min_str + ":" + sec_str + "." +milisec_str

# define event handlers for buttons; "Start", "Stop", "Reset"


# define event handler for timer with 0.1 sec interval

# define draw handler
def draw(canvas):
    canvas.draw_text(format(Time), [100, 110], 48, "White")
    canvas.draw_text(str(Num_Scores) + "/" + str(Num_Games), [250, 25], 28, "Green")

# define start button handler
def start_handler():
    global Num_Games, Timer_status
    if ( Timer_status == False):
        Num_Games += 1
        timer.start()
        Timer_status = 1


#define stop_button handler
def stop_handler():
    global Num_Games, Num_Scores, Time, Timer_status
    if ( Timer_status ):
        Timer_status = False
        if ( (Time  % 10) == 0):
            Num_Scores += 1
    timer.stop()

#define reset button handler
def reset_handler():
    global Time, Num_Games, Num_Scores, Timer_status
    Time = 0
    Num_Scores = 0
    Num_Games = 0
    Timer_status = False
    timer.stop()



def tick():
    global Time
    Time += 1
    return Time

# create frame
frame = simplegui.create_frame("Stop Watch", 300, 200)

# register event handlers
frame.set_draw_handler(draw)
frame.add_button('Start', start_handler, 100)
frame.add_button('Stop', stop_handler, 100)
frame.add_button('Reset', reset_handler, 100)

timer = simplegui.create_timer(interval, tick)

# Start the frame animation
frame.start()
