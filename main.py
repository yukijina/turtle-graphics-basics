from turtle import Turtle, Screen

speedy = Turtle()
print(speedy)

speedy.shape("turtle")
speedy.color("red")

def make_dashline(line_length, dash_length, num):
  for _ in range(0,num):
    speedy.pendown()
    speedy.forward(line_length)
    speedy.penup()
    speedy.forward(dash_length)


make_dashline(10, 5, 10)

# def make_square():
#   for _ in range(0,4):
#     speedy.forward(100)
    #speedy.right(90)


#make_square()

screen = Screen()
screen.exitonclick()