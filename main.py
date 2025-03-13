from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
print(timmy_the_turtle)

timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")


def make_square():
  for _ in range(0,4):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(90)


make_square()

screen = Screen()
screen.exitonclick()