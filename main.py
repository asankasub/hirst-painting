# import colorgram as cg

# colour_list = cg.extract('120123_r21786_g2048.jpg', 10^6)
# colour_palette = []

# for colour in colour_list:
#     r = colour.rgb.r
#     g = colour.rgb.g
#     b = colour.rgb.b
#     colour_palette.append((r, g, b))

# print(colour_palette)

colour_list = [ (1, 13, 31), (52, 25, 17), (219, 127, 106), (9, 105, 160), (242, 214, 69), (150, 84, 39), (215, 87, 64), (164, 162, 32)]
print(type(colour_list))
# 10 x 10
# dots 20 in size spaced apart by 50

import turtle
import random

turtle.colormode(255)
timmy = turtle.Turtle()
window = turtle.Screen()
timmy.shape("turtle")
timmy.color("green")
timmy.penup()
timmy.setx(-200)
y = -50
timmy.sety(y)
timmy.speed(0)
timmy.ht()

for i in range(10):
    
    for j in range(10):

        timmy.pendown()
        timmy.pencolor(random.choice(colour_list))
        timmy.dot(20)
        timmy.penup()
        timmy.forward(50)


    y += 50
    timmy.setx(-200)
    timmy.sety(y)



# timmy.setx(0)
# timmy.sety(50)
# timmy.forward(50)

window.exitonclick()
