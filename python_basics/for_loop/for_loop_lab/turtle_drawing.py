import turtle

colors = ['red', 'green', 'black', 'blue']
turtle.speed(2)
turtle.pensize(4)

for i in range(200):
    turtle.color(colors[i % 4])
    turtle.forward(i * 2)
    turtle.left(89)

turtle.done
