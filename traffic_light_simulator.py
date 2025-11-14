import turtle
import time
from typing import List, Dict

"""
Traffic Light Simulator

Refactored so you can create any number of lights per housing.

Usage:
 - Create TrafficLight(x, y, colors=[...], spacing=40)
 - Call run_simulation([tl1, tl2, ...], sequence=[...], durations={...},
                      blink_color='yellow', blink_times=5)

The example at the bottom recreates the three housings that were
previously in the file. Change positions or colors as needed.
"""


class TrafficLight:
    """A traffic-light housing with an arbitrary ordered list of lights.

    lights: list of color-names (strings). They will be stacked top->bottom
    around the given (x,y) center with the provided spacing.
    """

    def __init__(self, x: int, y: int, colors: List[str], spacing: int = 40,
                 housing_size=(6, 2)) -> None:
        self.x = x
        self.y = y
        self.colors = list(colors)
        self.spacing = spacing

        # Draw housing (simple square stretched to look like a vertical box)
        self.housing = turtle.Turtle()
        self.housing.hideturtle()
        self.housing.shape("square")
        self.housing.shapesize(stretch_wid=housing_size[0], stretch_len=housing_size[1])
        self.housing.penup()
        self.housing.goto(self.x, self.y)

        # Create light turtles and position them top -> bottom
        self.lights: Dict[str, turtle.Turtle] = {}
        n = len(self.colors)
        if n == 0:
            return

        top_y = self.y + ((n - 1) / 2.0) * self.spacing
        for i, color in enumerate(self.colors):
            t = turtle.Turtle()
            t.hideturtle()
            t.shape("circle")
            t.penup()
            t.speed(0)
            t.color("black")  # off state
            pos_y = top_y - i * self.spacing
            t.goto(self.x, pos_y)
            t.showturtle()
            self.lights[color] = t

    def _set_color_safe(self, t: turtle.Turtle, name: str) -> None:
        """Set color on turtle, with a safe fallback to hex if needed."""
        try:
            t.color(name)
        except turtle.TurtleGraphicsError:
            fallbacks = {"green": "#00FF00", "red": "#FF0000", "yellow": "#FFFF00"}
            t.color(fallbacks.get(name, "black"))

    def turn_on(self, color: str) -> None:
        if color in self.lights:
            self._set_color_safe(self.lights[color], color)

    def turn_off(self, color: str) -> None:
        if color in self.lights:
            self._set_color_safe(self.lights[color], "black")

    def blink(self, color: str, times: int = 5, on_time: float = 0.35, off_time: float = 0.25) -> None:
        if color not in self.lights:
            return
        t = self.lights[color]
        for _ in range(times):
            self._set_color_safe(t, color)
            time.sleep(on_time)
            self._set_color_safe(t, "black")
            time.sleep(off_time)


def run_simulation(traffic_lights: List[TrafficLight], sequence: List[str] = None,
                   durations: Dict[str, float] = None,
                   blink_color: str = "yellow", blink_times: int = 5,
                   blink_on: float = 0.35, blink_off: float = 0.25) -> None:
    """Run a simple synchronous simulation across all provided traffic lights.

    This runs an infinite loop. Each step turns the named color on for its
    duration on every traffic light that has that color, then turns it off.
    If the color equals blink_color, each light that supports it will blink
    `blink_times` times instead of staying on continuously.
    """
    if sequence is None:
        # default sequence: unified order from the union of colors in first light
        if not traffic_lights:
            return
        sequence = list(traffic_lights[0].colors)

    if durations is None:
        durations = {"red": 3.0, "yellow": 1.0, "green": 3.0}

    try:
        while True:
            for color in sequence:
                if color == blink_color:
                    # Blink on all lights that have this color
                    for tl in traffic_lights:
                        if color in tl.lights:
                            tl.blink(color, times=blink_times, on_time=blink_on, off_time=blink_off)
                    # short pause after the group blink
                    time.sleep(0.2)
                else:
                    # Turn on the color for each light that supports it
                    for tl in traffic_lights:
                        if color in tl.lights:
                            tl.turn_on(color)
                    time.sleep(durations.get(color, 1.0))
                    for tl in traffic_lights:
                        if color in tl.lights:
                            tl.turn_off(color)
                    time.sleep(0.2)
    except turtle.Terminator:
        # window closed by user
        pass


if __name__ == "__main__":
    # Example usage: recreate the three housings you had previously.
    LIGHT_SPACING = 40

    tl1 = TrafficLight(200, 100, colors=["red", "yellow", "green"], spacing=LIGHT_SPACING)
    tl2 = TrafficLight(100, 200, colors=["red", "yellow", "green"], spacing=LIGHT_SPACING)
    tl3 = TrafficLight(150, 150, colors=["red", "yellow", "green"], spacing=LIGHT_SPACING)
    tl4 = TrafficLight(-100, 0, colors=["red", "yellow", "green"], spacing=LIGHT_SPACING)
    # Run the simulation (this will block; close the Turtle window to stop)
    run_simulation([tl1, tl2, tl3, tl4], sequence=["red", "green", "yellow"],
                   durations={"red": 3.0, "green": 3.0, "yellow": 1.0},
                   blink_color="yellow", blink_times=5)
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