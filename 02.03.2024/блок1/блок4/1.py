import turtle as t


t_ = t.Turtle()
t.tracer(0)

m = 40

t_.left(90)
for i in range(15):
   t_.forward(4*m)
   t_.right(60)
t_.penup()


for x in range(-15, 20):
    for y in range(-25, 20):
        t_.setpos(x * m, y * m)
        t_.dot()

t.done()