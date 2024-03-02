import turtle as t

k = 20
t.tracer(0,0)


for i in range(2):
    t.forward(10 * k)
    t.right(90)
    t.forward(20 * k)
    t.right(90)
t.up()

t.forward(5 * k)
t.right(90)
t.back(10 * k)
t.left(90)


t.down()

for i in range(2):
    t.forward(20 * k)
    t.right(90)
    t.forward(40 * k)
    t.right(90)
t.up()

for x in range(-20, 20):
    for y in range(-20, 20):
        t.goto(x*k, y*k)
        if x==0 or y==0:
            t.dot(6)
        else:
            t.dot(4)

t.update()
t.mainloop()