# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400
<<<<<<< HEAD
BALL_RADIUS = 20
=======
BALL_RADIUS = 10
>>>>>>> FETCH_HEAD
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

<<<<<<< HEAD
acc1 = 0
acc2 = 0
ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [-120.0 / 60.0, 6.0 / 60.0]
=======
interval = 10000
speed_multiplier = 1

acc1 = 0
acc2 = 0
ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [-150.0 / 60.0, 10.0 / 60.0]
>>>>>>> FETCH_HEAD

paddle1_pos = [0, HEIGHT / 2 - PAD_HEIGHT / 2]
paddle2_pos = [WIDTH, HEIGHT / 2 - PAD_HEIGHT / 2]
paddle1_vel = [0, 0]
paddle2_vel = [0, 0]

<<<<<<< HEAD
=======

def start():
    global ball_pos, ball_vel, paddle1_pos, paddle2_pos, speed_multiplier, paddle1_vel, paddle2_vel
    paddle1_vel = [0, 0]
    paddle2_vel = [0, 0]
    speed_multiplier = 1
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    ball_vel = [-150.0 / 60.0, 10.0 / 60.0]
    paddle1_pos = [0, HEIGHT / 2 - PAD_HEIGHT / 2]
    paddle2_pos = [WIDTH, HEIGHT / 2 - PAD_HEIGHT / 2]
    new_game()

def reset():
    global ball_pos, ball_vel, paddle1_pos, paddle2_pos, speed_multiplier
    speed_multiplier = 1
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    ball_vel = [0, 0]
    paddle1_pos = [0, HEIGHT / 2 - PAD_HEIGHT / 2]
    paddle2_pos = [WIDTH, HEIGHT / 2 - PAD_HEIGHT / 2]
    new_game()


def stop():
    global ball_vel
    ball_vel = [0, 0]

>>>>>>> FETCH_HEAD
# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists


# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    score1 = 0
    score2 = 0
<<<<<<< HEAD
    ball_pos = [WIDTH / 2, HEIGHT / 2]

# define event handlers for buttons; "Start", "Stop", "Reset"

def start_handler():
    global paddle1_pos, paddle2_pos, ball_vel
    ball_vel = [-120.0 / 60.0, 10.0 / 60.0]
    paddle1_pos = [0, HEIGHT / 2 - PAD_HEIGHT / 2]
    paddle2_pos = [WIDTH, HEIGHT / 2 - PAD_HEIGHT / 2]
    
    
#def stop_handler():
    
def reset_handler():    
  new_game()




def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, acc1, acc2, paddle1_vel, paddle2_vel
=======

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
>>>>>>> FETCH_HEAD


    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")

    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    # collide and reflect off of left hand side of canvas
<<<<<<< HEAD
    if ball_pos[0] <= PAD_WIDTH + BALL_RADIUS:
        if paddle1_pos[1] <= ball_pos[1] <= (paddle1_pos[1] + PAD_HEIGHT):
            ball_vel[0] = - ball_vel[0]

        elif ball_pos[0] <= 0:
            score2 = score2 + 1      
            ball_pos = [WIDTH / 2, HEIGHT / 2]

    if score2 >= 5:
        canvas.draw_text(("Game over!!!"), [100,100], 20, "White")
        ball_vel = [0, 0]            

    # collide and reflect off of right hand side of canvas
    if ball_pos[0] >= WIDTH -1 -BALL_RADIUS - PAD_WIDTH:
        if paddle2_pos[1] <= ball_pos[1] <= (paddle2_pos[1] + PAD_HEIGHT):
            ball_vel[0] = - ball_vel[0]

        elif ball_pos[0] >= WIDTH -1:
            score1 = score1 + 1      
            ball_pos = [WIDTH / 2, HEIGHT / 2]
        
    if score1 >= 5:
        canvas.draw_text(("Game over!!!"), [450,100], 20, "White")
        ball_vel = [0, 0]
        
=======
    if ball_pos[0] <= PAD_WIDTH + BALL_RADIUS and (paddle1_pos[1] <= ball_pos[1]<= paddle1_pos[1] + PAD_HEIGHT):
        ball_vel[0] = - ball_vel[0]
    elif ball_pos[0] <= PAD_WIDTH + BALL_RADIUS:
        score2 = score2 + 1
        speed_multiplier = 1
        ball_vel = [-150.0 / 60.0, 10.0 / 60.0]
        ball_pos = [WIDTH / 2, HEIGHT / 2]


    # collide and reflect off of right hand side of canvas
    if ball_pos[0] >= WIDTH -1 -BALL_RADIUS - PAD_WIDTH  and (paddle2_pos[1] <= ball_pos[1]<= paddle2_pos[1] + PAD_HEIGHT):
        ball_vel[0] = - ball_vel[0]
    elif ball_pos[0] >= WIDTH -1 -BALL_RADIUS - PAD_WIDTH:
        score1 = score1 + 1
        speed_multiplier = 1
        ball_vel = [-150.0 / 60.0, 10.0 / 60.0]
        ball_pos = [WIDTH / 2, HEIGHT / 2]
>>>>>>> FETCH_HEAD

    # collide and reflect off of bottom side of canvas
    if ball_pos[1] >= HEIGHT-1 - BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]

    # collide and reflect off of top side of canvas
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]

    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")

    # update paddle's vertical position, keep paddle on the screen
    # check collision on bottom of canvas
<<<<<<< HEAD
    if paddle1_pos[1] >= HEIGHT - paddle1_pos[1]:
        paddle1_vel[1] = 0
    else:
        paddle1_vel[1] += acc1

    # check collision on top of canvas
    if paddle1_pos[1] <= 0:
        paddle1_vel[1] = 0
    else:
        paddle1_vel[1] -= acc1
    # check collision on bottom of canvas
    if paddle2_pos[1] >= HEIGHT - paddle2_pos[1]:
        paddle2_vel[1] = 0
    else:
        paddle2_vel[1] += acc2

    # check collision on top of canvas
    if paddle2_pos[1] <= 0:
        paddle2_vel[1] = 0
    else:
        paddle2_vel[1] -= acc2
=======
    if paddle1_pos[1] >= HEIGHT - PAD_HEIGHT:
        paddle1_pos[1] = HEIGHT - PAD_HEIGHT
    # check collision on top of canvas
    if paddle1_pos[1] <= 0:
        paddle1_pos[1] = 0
    # check collision on bottom of canvas
    if paddle2_pos[1] >= HEIGHT - PAD_HEIGHT:
        paddle2_pos[1] = HEIGHT - PAD_HEIGHT
    # check collision on top of canvas
    if paddle2_pos[1] <= 0:
        paddle2_pos[1] = 0
>>>>>>> FETCH_HEAD

    paddle1_pos[0] += paddle1_vel[0]
    paddle1_pos[1] += paddle1_vel[1]

    paddle2_pos[0] += paddle2_vel[0]
    paddle2_pos[1] += paddle2_vel[1]

    # draw paddles
    canvas.draw_polygon([paddle1_pos,
                         (0, paddle1_pos[1] + PAD_HEIGHT),
                         (PAD_WIDTH, paddle1_pos[1] + PAD_HEIGHT),
                         (PAD_WIDTH, paddle1_pos[1])], 2, "Fuchsia")

    canvas.draw_polygon([paddle2_pos,
                         (WIDTH, paddle2_pos[1] + PAD_HEIGHT),
                         (WIDTH - PAD_WIDTH, paddle2_pos[1] + PAD_HEIGHT),
                         (WIDTH - PAD_WIDTH, paddle2_pos[1])], 2, "Green")

<<<<<<< HEAD

=======
>>>>>>> FETCH_HEAD
    # draw scores
    canvas.draw_text(str(score1),[WIDTH/4,HEIGHT/3],20, "White")
    canvas.draw_text(str(score2),[3*WIDTH/4,HEIGHT/3],20, "White")


<<<<<<< HEAD
def keydown(key):
    global paddle1_vel, paddle2_vel, acc1, acc2
    acc1 = 1
    acc2 = 1
    if key==simplegui.KEY_MAP["down"]:
        # check collision on bottom of canvas
        if paddle1_pos[1] >= HEIGHT - paddle1_pos[1]:
            paddle1_vel[1] = 0
        else:
            paddle1_vel[1] += acc1
    elif key==simplegui.KEY_MAP["up"]:
        # check collision on top of canvas
        if paddle1_pos[1] <= 0:
            paddle1_vel[1] = 0
        else:
            paddle1_vel[1] -= acc1
    elif key==simplegui.KEY_MAP["2"]:
        # check collision on bottom of canvas
        if paddle2_pos[1] >= HEIGHT - paddle2_pos[1]:
            paddle2_vel[1] = 0
        else:
            paddle2_vel[1] += acc2

    elif key==simplegui.KEY_MAP["8"]:
        # check collision on top of canvas
        if paddle2_pos[1] <= 0:
            paddle2_vel[1] = 0
        else:
            paddle2_vel[1] -= acc2
=======
    if score1 >= 5:
        canvas.draw_text("Game over!",[50, HEIGHT/4],30, "Fuchsia")
        stop()
    if score2 >= 5:
        canvas.draw_text("Game over!",[350, HEIGHT/4],30, "Green")
        stop()


def keydown(key):
    global paddle1_vel, paddle2_vel, acc1, acc2
    acc1 = 2
    acc2 = 2
    if key==simplegui.KEY_MAP["down"]:
        paddle1_vel[1] += acc1
    elif key==simplegui.KEY_MAP["up"]:
        paddle1_vel[1] -= acc1
    elif key==simplegui.KEY_MAP["2"]:
        paddle2_vel[1] += acc2
    elif key==simplegui.KEY_MAP["8"]:
        paddle2_vel[1] -= acc2
>>>>>>> FETCH_HEAD

    print paddle1_pos
    print paddle2_pos


<<<<<<< HEAD

=======
>>>>>>> FETCH_HEAD
def keyup(key):
    global paddle1_vel, paddle2_vel, acc1, acc2

    if key==simplegui.KEY_MAP["down"]:
<<<<<<< HEAD
        # check collision on bottom of canvas
        if paddle1_pos[1] >= HEIGHT - paddle1_pos[1]:
            paddle1_vel[1] = 0
        else:
            paddle1_vel[1] -= acc1
    elif key==simplegui.KEY_MAP["up"]:
        # check collision on top of canvas
        if paddle1_pos[1] <= 0:
            paddle1_vel[1] = 0
        else:
            paddle1_vel[1] += acc1
    elif key==simplegui.KEY_MAP["2"]:
        # check collision on bottom of canvas
        if paddle2_pos[1] >= HEIGHT - paddle2_pos[1]:
            paddle2_vel[1] = 0
        else:
            paddle2_vel[1] -= acc2
    elif key==simplegui.KEY_MAP["8"]:
        # check collision on top of canvas
        if paddle2_pos[1] <= 0:
            paddle2_vel[1] = 0
        else:
            paddle2_vel[1] += acc2

=======
      paddle1_vel[1] -= acc1
    elif key==simplegui.KEY_MAP["up"]:
      paddle1_vel[1] += acc1
    elif key==simplegui.KEY_MAP["2"]:
      paddle2_vel[1] -= acc2
    elif key==simplegui.KEY_MAP["8"]:
      paddle2_vel[1] += acc2

# Handler for timer
def tick():
    global bal_vel, speed_multiplier
    speed_multiplier = speed_multiplier + 0.5
    ball_vel[0] = speed_multiplier*ball_vel[0]
    ball_vel[1] = speed_multiplier*ball_vel[1]
>>>>>>> FETCH_HEAD


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
<<<<<<< HEAD

button1 = frame.add_button("Start", start_handler, 50)
#button2 = frame.add_button("Stop", stop_handler, 50)
button3 = frame.add_button("Reset", reset_handler, 50)


frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
=======
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
timer = simplegui.create_timer(interval, tick)
>>>>>>> FETCH_HEAD


# start frame
new_game()
<<<<<<< HEAD
frame.start()
=======
frame.start()
timer.start()
>>>>>>> FETCH_HEAD
