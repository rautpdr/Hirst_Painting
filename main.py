import random
from turtle import Turtle , Screen
import colorgram


color = colorgram.extract("image.jpg" , 30)
color_palate = []

for c in color:
    r = c.rgb.r
    g = c.rgb.g
    b = c.rgb.b
    new = (r,g,b)
    color_palate.append(new)

print(color_palate)







#setting up turtle
tim_turtle = Turtle()
screen =Screen()
tim_turtle.penup()
tim_turtle.hideturtle()
tim_turtle.speed("fastest")

screen.colormode(255)




rgb_colors = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241),
              (236, 239, 243), (149, 75, 50), (222, 201, 136),
              (53, 93, 123), (170, 154, 41), (138, 31, 20),
              (134, 163, 184), (197, 92, 73), (47, 121, 86),
              (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50),
              (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19),
              (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

def printing_image():
    tim_turtle.setheading(225)
    tim_turtle.forward(300)
    tim_turtle.setheading(0)

    #to make 10*10 grid
    for row in range(10):
        for col in range(10):
            tim_turtle.dot(20 , random.choice(rgb_colors))
            tim_turtle.forward(50)

        tim_turtle.setheading(90)
        tim_turtle.forward(50)      # space between rows
        tim_turtle.setheading(180)
        tim_turtle.forward(500)     # go back to start of the row
        tim_turtle.setheading(0)

printing_image()
screen.exitonclick()
