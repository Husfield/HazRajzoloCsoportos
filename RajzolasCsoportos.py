import turtle

turtle.speed(0)
turtle.width(3)

fordulas=45
szog = 90
hossz = 100
i = 0

while i < 4:
    turtle.forward(hossz)
    turtle.left(szog)
    i += 1

turtle.left(szog)
turtle.forward(hossz)


j=0
while j<2:
    turtle.right(fordulas)
    turtle.forward(hossz)
    turtle.right(fordulas)
    j+=1

turtle.done()