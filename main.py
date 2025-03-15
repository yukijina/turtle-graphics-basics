from turtle import Turtle, Screen
import random

speedy = Turtle()
print(speedy)

speedy.shape("turtle")
speedy.color("spring green")

def draw_dashline(line_length, dash_length, num):
  """draw a dashline with length of the parameter"""
  for _ in range(0,num):
    speedy.pendown()
    speedy.forward(line_length)
    speedy.penup()
    speedy.forward(dash_length)
    
#draw_dashline(10, 5, 10)

def draw_square(line_length):
  """draw a squre shape with length of the parameter"""
  for _ in range(0,4):
    speedy.forward(line_length)
    speedy.right(90)

#draw_square(100)

def draw_pentagon(line_length):
  """draw a pentagon shape"""
  for _ in range(0,5):
    speedy.right(72)
    speedy.forward(line_length)

#draw_pentagon(150)


color_pallets = ["aquamarine", "green", "orange", "pink", "coral", "orchid", "gold"]

def draw_shape(side_num, line_length):
  """draw any shape by incresing 1 side of the shape"""
  angle = 360 / side_num
  for _ in range(0,side_num):
    speedy.right(angle)
    speedy.forward(line_length)
    
  for _ in range(3,11):
    speedy.color(random.choice(color_pallets))

# draw_shape(shape_side_num, 100)
  
  
def draw_a_random_walk():
  """turtle walk in a random direction"""
  speedy.pensize(10)
  speedy.speed("fast")
  direction = [0, 90,180,270]

  for _ in range(80):
    speedy.setheading(random.choice(direction)) 
    speedy.pencolor(random.choice(color_pallets))
    speedy.forward(20)
   
draw_a_random_walk()


screen = Screen()
screen.exitonclick()