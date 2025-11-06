import turtle
import time

# Screen setup
screen = turtle.Screen()
screen.title("Traffic Light Simulator")
# Traffic light setup (housing)
# Set the housing center here to move the whole traffic light at once
HOUSING_X, HOUSING_Y = 0, 0  # change these values to move the traffic light
HOUSING_1_X, HOUSING_1_Y = 100, 0
HOUSING_2_X, HOUSING_2_Y = -100, 0
LIGHT_SPACING = 40                # vertical spacing between lights

housing = turtle.Turtle()
housing.shape("square")
housing.shapesize(stretch_wid=6, stretch_len=2)
housing.penup()
housing.goto(HOUSING_X, HOUSING_Y)

housing_1 = turtle.Turtle()
housing_1.shape("square")
housing_1.shapesize(stretch_wid=6, stretch_len=2)
housing_1.penup()
housing_1.goto(HOUSING_1_X, HOUSING_1_Y)

housing_2 = turtle.Turtle()
housing_2.shape("square")
housing_2.shapesize(stretch_wid=6, stretch_len=2)
housing_2.penup()
housing_2.goto(HOUSING_2_X, HOUSING_2_Y)

# Light colors (circle turtles) - create and position top->middle->bottom
red_light = turtle.Turtle()
yellow_light = turtle.Turtle()
green_light = turtle.Turtle()

red_light_1 = turtle.Turtle()
yellow_light_1 = turtle.Turtle()
green_light_1 = turtle.Turtle()

red_light_2 = turtle.Turtle()
yellow_light_2 = turtle.Turtle()
green_light_2 = turtle.Turtle()


# Position the lights relative to the housing center: top, middle, bottom
red_light.goto(HOUSING_X, HOUSING_Y + LIGHT_SPACING)
yellow_light.goto(HOUSING_X, HOUSING_Y)
green_light.goto(HOUSING_X, HOUSING_Y - LIGHT_SPACING)

red_light_1.goto(HOUSING_1_X, HOUSING_1_Y + LIGHT_SPACING)
yellow_light_1.goto(HOUSING_1_X, HOUSING_1_Y)
green_light_1.goto(HOUSING_1_X, HOUSING_1_Y - LIGHT_SPACING)

red_light_2.goto(HOUSING_2_X, HOUSING_2_Y + LIGHT_SPACING)
yellow_light_2.goto(HOUSING_2_X, HOUSING_2_Y)
green_light_2.goto(HOUSING_2_X, HOUSING_2_Y - LIGHT_SPACING)


for t in (red_light_1, yellow_light_1, green_light_1):
    t.shape("circle")
    t.color("black")   # off state
    t.penup()
    t.speed(0)

for t in (red_light_2, yellow_light_2, green_light_2):
    t.shape("circle")
    t.color("black")   # off state
    t.penup()
    t.speed(0)  

for t in (red_light, yellow_light, green_light):
    t.shape("circle")
    t.color("black")   # off state
    t.penup()
    t.speed(0)

durations = {"red": 3.0, "yellow": 1.0, "green": 3.0}

# Simple simulation loop: red -> green -> yellow
lights = {"red": red_light, "green": green_light, "yellow": yellow_light}
lights_1 = {"red": red_light_1, "green": green_light_1, "yellow": yellow_light_1}
lights_2 = {"red": red_light_2, "green": green_light_2, "yellow": yellow_light_2}

try:
    while True:
        for color in lights:
            if color == "yellow":
                # The yellow light blinks 5 times
                for _ in range(5):
                    lights["yellow"].color("yellow")
                    time.sleep(0.35)
                    lights["yellow"].color("black")
                    time.sleep(0.25)
                # short pause after each blink
                time.sleep(0.2)
            else:
                lights[color].color(color)      # turn on
                time.sleep(durations[color])
                lights[color].color("black")  # turn off
                time.sleep(0.2)
        for color in lights_1:
            if color == "yellow":
                # The yellow light blinks 5 times
                for _ in range(5):
                    lights_1["yellow"].color("yellow")
                    time.sleep(0.35)
                    lights_1["yellow"].color("black")
                    time.sleep(0.25)
                # short pause after each blink
                time.sleep(0.2)
            else:
                lights_1[color].color(color)      # turn on
                time.sleep(durations[color])
                lights_1[color].color("black")  # turn off
                time.sleep(0.2)
        for color in lights_2:
            if color == "yellow":
                # The yellow light blinks 5 times
                for _ in range(5):
                    lights_2["yellow"].color("yellow")
                    time.sleep(0.35)
                    lights_2["yellow"].color("black")
                    time.sleep(0.25)
                # short pause after each blink
                time.sleep(0.2)
            else:
                lights_2[color].color(color)      # turn on
                time.sleep(durations[color])
                lights_2[color].color("black")  # turn off
                time.sleep(0.2)
except turtle.Terminator:
    # window closed
    pass
screen.bye()