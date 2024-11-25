import turtle
CANNON_STEP = 10

window = turtle.Screen()
window.setup(0.5, 0.75)
window.bgcolor(0.2, 0.2, 0.2)
window.title("The Real Python Space Invaders")

LEFT = -window.window_width() / 2
RIGHT = window.window_width() / 2
TOP = window.window_height() / 2
BOTTOM = -window.window_height() / 2
FLOOR_LEVEL = 0.9 * BOTTOM

# Create laser cannon
cannon = turtle.Turtle()

cannon.penup()
cannon.color(1, 1, 1)
cannon.shape("square")

# Draw cannon
cannon.turtlesize(1, 4)  # Base
cannon.stamp()
cannon.sety(FLOOR_LEVEL + 10)
cannon.turtlesize(1, 1.5)  # Next tier
cannon.stamp()
cannon.sety(FLOOR_LEVEL + 20)
cannon.turtlesize(0.8, 0.3)  # Tip of cannon
cannon.stamp()
cannon.sety(FLOOR_LEVEL)

cannon.setposition(0, FLOOR_LEVEL)

def move_left():
    cannon.setx(cannon.xcor() - CANNON_STEP)

def move_right():
    cannon.setx(cannon.xcor() + CANNON_STEP)

window.onkeypress(move_left, "Left")
window.onkeypress(move_right, "Right")
window.onkeypress(turtle.bye, "q")
window.listen()

turtle.done()