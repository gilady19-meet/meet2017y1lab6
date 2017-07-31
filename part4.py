UP_ARROW = "Up"
LEFT_ARROW = "Left"
DOWN_ARROW = "Down"
RIGHT_ARROW = "Right"
UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3

direction = UP

def up():
    global direction
    direction = UP
    print ('you pressed Up!')

def left():
    global direction
    direction = LEFT
    print ('you pressed Left!')

def down():
    global direction
    direction = DOWN
    print ('you pressed Down!')

def right():
    global direction
    direction = RIGHt
    print ('you pressed Right!')
