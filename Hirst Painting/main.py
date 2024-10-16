# import colorgram
# colors = colorgram.extract("image1.jpg", 30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
import turtle
from turtle import Turtle, Screen
import random

from PIL.ImageChops import screen

colors = [(236, 224, 80), (197, 7, 71), (195, 164, 13), (201, 75, 15), (231, 54, 132), (110, 179, 216), (217, 163, 101), (27, 105, 168), (35, 186, 109), (19, 29, 168), (13, 23, 66), (212, 135, 177), (233, 223, 7), (199, 33, 132), (13, 183, 212), (230, 166, 199), (126, 189, 162), (8, 49, 28), (40, 132, 77), (128, 219, 232), (58, 12, 25), (67, 22, 7), (114, 90, 210), (146, 216, 199), (179, 17, 8), (233, 66, 34)]
turtle.colormode(255)
timmy_the_turtle = Turtle()
timmy_the_turtle.speed("fastest")
timmy_the_turtle.penup()
timmy_the_turtle.setheading(225)
timmy_the_turtle.forward(250)
timmy_the_turtle.setheading(0)
num_dots = 100
for dot_count in range(1, num_dots + 1):
    timmy_the_turtle.dot(20, random.choice(colors))
    timmy_the_turtle.forward(50)
    if dot_count % 10 == 0:
        timmy_the_turtle.setheading(90)
        timmy_the_turtle.forward(50)
        timmy_the_turtle.setheading(180)
        timmy_the_turtle.forward(500)
        timmy_the_turtle.setheading(0)
timmy_the_turtle.hideturtle()

screen = Screen()
screen.exitonclick()