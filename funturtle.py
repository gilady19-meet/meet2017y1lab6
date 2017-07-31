import turtle
turtle.shape('turtle')
square = turtle.clone()
square.shape('triangle')
square.goto(100,100)
square.stamp()
square.goto(200,0)
square.stamp()
square.goto(0,0)
square.stamp()

turtle.shape('turtle')
square.shape('triangle')
square.goto(300,0)
square.goto(300,300)
square.stamp()
square.goto(100,100)

turtle.mainloop()
