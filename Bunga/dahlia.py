import turtle

turtle.bgcolor('black')
turtle.speed(80)
turtle.hideturtle()

colors = ["#3C8FE8", "#3C33F5", "#3662FF", "#36CCFF"]

for i in range(120):
    for c in colors:
        turtle.color(c)
        turtle.circle(180-i, 100)
        turtle.lt(90)
        turtle.circle(180-i, 100)
        turtle.end_fill()

turtle.mainloop()