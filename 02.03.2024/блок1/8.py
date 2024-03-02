import turtle as t

k = 20
t. tracer(0, 0)
t.left(90)

for _ in range(7):
    t.goto(t.pos()+t.Vec2D(6, -9) * k)
    t.goto(t.pos()+t.Vec2D(-6, 2) * k)
    t.goto(t.pos()+t.Vec2D(12, 3) * k)
t.up()

for x in range(-20, 20):
    for y in range(-20, 20):
        t.goto(x * k, y * k)
        t.dot(4)
t.update()
t.mainloop()