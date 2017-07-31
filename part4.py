import turtle
turtle.pendown

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
    global up
    direction = UP
    print(direction)
    return ('you pressed Up!')

def left():
    global direction
    global left
    direction = LEFT
    print(direction)
    return ('you pressed left!')

def down():
    global direction
    global down
    direction = DOWN
    print(direction)
    return ('you pressed down!')

def right():
    global direction
    global right
    direction = RIGHT
    print(direction)
    return ('you pressed right!')

turtle.onkeypress(up, UP_ARROW)
turtle.onkeypress(down, DOWN_ARROW)
turtle.onkeypress(right, RIGHT_ARROW)
turtle.onkeypress(left, LEFT_ARROW)
turtle.pendown
turtle.listen()

turtle.mainloop                                                                                                                                                                                                 
