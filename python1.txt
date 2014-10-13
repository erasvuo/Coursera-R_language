# control the velocity of a ball using the arrow keys

import simplegui

# Initialize globals
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20

ball_pos = [WIDTH / 2, HEIGHT / 2]
vel = [0, 0]
acc = 0

# define event handlers
def draw(canvas):

    # gone out from left hand side of canvas and visible from right side
    if ball_pos[0] <= 0:
        ball_pos[0] = WIDTH - 1 + vel[0]
        ball_pos[1] += vel[1]
    # gone out from right hand side of canvas and visible from left side
    elif ball_pos[0] >= WIDTH - 1:
        ball_pos[0] = 0 + vel[0]
        ball_pos[1] += vel[1]

    # gone out from top of canvas and visible from bottom side
    elif ball_pos[1] <= 0:
        ball_pos[1] = HEIGHT - 1 + vel[1]
        ball_pos[0] += vel[0]

    # gone out from bottom of canvas and visible from top side
    elif ball_pos[1] >= HEIGHT - 1:
        ball_pos[1] = 0 + vel[1]
        ball_pos[0] += vel[0]

    else:
        # Update ball position
        ball_pos[0] += vel[0]
        ball_pos[1] += vel[1]

    # Draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")

def keydown(key):
    global acc
    acc = 1
    if key==simplegui.KEY_MAP["left"]:
        vel[0] -= acc
    elif key==simplegui.KEY_MAP["right"]:
        vel[0] += acc
    elif key==simplegui.KEY_MAP["down"]:
        vel[1] += acc
    elif key==simplegui.KEY_MAP["up"]:
        vel[1] -= acc

    print ball_pos

def keyup(key):
    global acc
    if key==simplegui.KEY_MAP["left"]:
        vel[0] += acc
    elif key==simplegui.KEY_MAP["right"]:
        vel[0] -= acc
    elif key==simplegui.KEY_MAP["down"]:
        vel[1] -= acc
    elif key==simplegui.KEY_MAP["up"]:
        vel[1] += acc

# create frame
frame = simplegui.create_frame("Velocity ball control", WIDTH, HEIGHT)

# register event handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

# start frame
frame.start()
