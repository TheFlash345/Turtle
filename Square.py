import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("Magenta")
    
    brad = turtle.Turtle()
    brad.shape("square")
    brad.color("yellow")
    brad.speed(1)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)

    Fadil = turtle.Turtle()
    Fadil.shape("classic")
    Fadil.color("purple")
    Fadil.circle(50)

    window.exitonclick()

draw_square()

