import turtle

# Setup the screen and turtle
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Flower with Turtle")

flower = turtle.Turtle()
flower.shape("turtle")
flower.speed(10)
flower.color("purple", "yellow")

def draw_petal():
    """Draws a single petal."""
    flower.circle(100, 60)  # Draw an arc
    flower.left(120)        # Turn the turtle
    flower.circle(100, 60)  # Draw another arc
    flower.left(120)        # Reset position

# Draw the flower by repeating petals
flower.penup()
flower.goto(0, -100)
flower.pendown()
flower.begin_fill()

for _ in range(6):  # Six petals
    draw_petal()
    flower.right(60)  # Rotate for the next petal

flower.end_fill()

# Draw the stem
flower.color("green")
flower.penup()
flower.goto(0, -100)
flower.pendown()
flower.right(90)
flower.forward(200)

# Draw a leaf on the stem
flower.penup()
flower.goto(0, -200)
flower.pendown()
flower.left(45)
flower.begin_fill()
flower.circle(50, 90)  # Leaf arc
flower.left(90)
flower.circle(50, 90)  # Other side of the leaf
flower.end_fill()

# End
flower.hideturtle()
screen.mainloop()
