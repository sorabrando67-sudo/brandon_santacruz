import turtle

t = turtle.Turtle()
t.speed(0)

for i in range(36):
    for j in range(6):
        t.forward(100)
        t.right(60)
    t.right(10)

turtle.done()