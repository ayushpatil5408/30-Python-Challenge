import turtle
import colorsys
import math
import random

screen = turtle.Screen()
screen.setup(900, 950)
screen.bgcolor("black")
screen.title("Rainbow Cosmic Spirograph")
screen.tracer(0)
screen.setworldcoordinates(-450, -450, 450, 450)

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

stars = turtle.Turtle()
stars.speed(0)
stars.hideturtle()
stars.penup()

random.seed(42)

star_data = []

for i in range(140):

    angle = random.uniform(0, math.pi * 2)
    radius = random.uniform(315, 430)

    x = math.cos(angle) * radius
    y = math.sin(angle) * radius

    star_data.append({
        "x": x,
        "y": y,
        "phase": random.uniform(0, math.pi * 2),
        "speed": random.uniform(0.5, 2.0),
        "size": random.uniform(1, 3),
        "color": random.choice([
            (0.8, 0.9, 1.0),
            (0.7, 0.8, 1.0),
            (1.0, 0.85, 1.0),
            (1.0, 1.0, 1.0)
        ])
    })

time = 0
LINES = 180

def draw_stars():

    stars.clear()

    for star in star_data:

        brightness = (
            0.45 + 0.55 *
            (math.sin(time * star["speed"] + star["phase"]) ** 2)
        )

        base_color = star["color"]

        color = (
            base_color[0] * brightness,
            base_color[1] * brightness,
            base_color[2] * brightness
        )

        size = star["size"] * brightness

        stars.goto(star["x"], star["y"])
        stars.dot(size, color)

def animate():

    global time

    t.clear()

    draw_stars()

    factor = 3 + math.sin(time * 0.2) * 2

    for i in range(LINES):

        angle = i * (math.pi * 2) / LINES

        hue = (
            angle / (math.pi * 2) + time * 0.1
        ) % 1.0

        color = colorsys.hsv_to_rgb(
            hue, 0.8, 1.0
        )

        t.pencolor(color)
        t.pensize(1)

        core_radius = 80 + math.sin(
            time * 2 + angle * 4
        ) * 20

        x1 = math.cos(angle + time) * core_radius
        y1 = math.sin(angle + time) * core_radius

        outer_radius = 280 + math.cos(
            time + angle * 3
        ) * 30

        x2 = math.cos(angle * factor) * outer_radius
        y2 = math.sin(angle * factor) * outer_radius

        t.penup()
        t.goto(x1, y1)
        t.pendown()
        t.goto(x2, y2)

        t.penup()
        t.goto(x2, y2)
        t.dot(4, color)

    time += 0.025

    screen.update()

    screen.ontimer(animate, 25)

try:
    animate()
    screen.mainloop()

except turtle.Terminator:
    pass
