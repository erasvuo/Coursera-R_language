# implementation of card game - Memory

import simplegui
import random

cardlist = [1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8]
exposed = ["False","False","False","False","False","False","False","False",
           "False","False","False","False","False","False","False","False"]
START_X = 20
START_Y = 20
CARD_HEIGHT = 60
CARD_WIDTH = 40
NUM_POS_X = 30
NUM_POS_Y = 60
flipped1 = 17
flipped2 = 15


def search_flipped(flipped):
    i = 0
    for num in cardlist:
        if cardlist[i] == flipped:
            init_one_exposed(i)
        i = i + 1

        
def init_exposed():
    i = 0
    for num in exposed:
        exposed[i] = "False"
        i = i + 1

def init_one_exposed(index):
    exposed[index] = "False"
    

# helper function to initialize globals
def new_game():
    global state
    state = 0
    init_exposed()
    random.shuffle(cardlist)
    
    
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state, flipped1, flipped2
    num = 0
    for i in cardlist:
        if (START_X + num * CARD_WIDTH < pos[0] < START_X + num * CARD_WIDTH + CARD_WIDTH
        and START_Y < pos [1] < START_Y + CARD_HEIGHT):

            if state == 0:
                state = 1
                exposed[num] = "True"
                flipped1 = cardlist[num]
            elif state == 1:
                state = 2
                exposed[num] = "True"
                flipped2 = cardlist[num]
            else:
                if flipped1 == flipped2:
                    pass
                else:
                    search_flipped(flipped1)                   
                    search_flipped(flipped2)                                      
                state = 1
                exposed[num] = "True"
                flipped1 = cardlist[num]
                flipped2 = 15
        num = num + 1
        
        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global state
    num = 0
    for i in cardlist:
        canvas.draw_polygon([[START_X + num * CARD_WIDTH, START_Y], 
                            [START_X + num * CARD_WIDTH, START_Y + CARD_HEIGHT], 
                            [START_X + num * CARD_WIDTH + CARD_WIDTH, START_Y + CARD_HEIGHT], 
                            [START_X + num * CARD_WIDTH + CARD_WIDTH, START_Y]], 2, 'White', 'Black')


        if exposed[num] == "True":
            canvas.draw_text(str(cardlist[num]), [NUM_POS_X + num * CARD_WIDTH, NUM_POS_Y], 30, "White")

            
            
        num = num + 1
    
    canvas.draw_text(str(state) + " card exposed", [30, 120], 24, "White")	

    
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 150)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric