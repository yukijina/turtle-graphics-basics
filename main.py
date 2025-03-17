from turtle import Turtle, Screen
import random

speedy = Turtle()
print(speedy)

screen = Screen()

speedy.shape("turtle")
speedy.color("spring green")
screen.colormode(255)

def random_color():
  """Generate a random color and return as a rgb list"""
  r = random.randint(0,255)
  g = random.randint(0,255)
  b = random.randint(0,255)
  
  rgb_color = (r,g,b)
  return rgb_color

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
    speedy.pencolor(random_color())
    speedy.forward(20)
   
#draw_a_random_walk()

def draw_spirograph(size_of_gap):
  """draw a spirograph shape"""
  speedy.speed("fastest")
  
  for _ in range(int(360 / size_of_gap)):
    speedy.circle(50)
    speedy.setheading(speedy.heading() + size_of_gap)
    speedy.pencolor(random_color())

#draw_spirograph(10)


def walk_circle():  
  """ turtle walk in circle"""
  speedy.shapesize(2,2)
  speedy.fillcolor("")
  speedy.speed("fast")
  
  for angle in range(360):
    speedy.setheading(angle)
    speedy.pencolor(random_color())
    speedy.forward(3)
    speedy.stamp()
    
#walk_circle()
  

def draw_dot_painting(dot_size, space_between_dot):
  """draw a dot painting from left to right with a random color"""
  speedy.color("")
  speedy.goto(-200, -100)
  
  def set_heading(angle, space_between_dot):
    speedy.setheading(90)
    speedy.forward(space_between_dot)
    speedy.setheading(angle)
    speedy.forward(space_between_dot)
 
  for counter in range(10):
    
    for _ in range(10):
      speedy.dot(dot_size, random_color())
      speedy.stamp()
      speedy.forward(space_between_dot)
      
    if counter == 0 or not counter % 2:
      #turn left
      set_heading(180, space_between_dot)
    else:
      #turn right
      set_heading(0, space_between_dot)

    
draw_dot_painting(20, 40)

screen.exitonclick()