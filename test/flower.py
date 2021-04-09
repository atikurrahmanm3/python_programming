import turtle as t
t.speed(5)
counter = 0

while counter <36:
    for i in range(4):
        t.forward(100)
        t.left(90)
    t.right(10)
    counter +=1

t.done()