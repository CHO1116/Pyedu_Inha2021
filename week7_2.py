import turtle as t

t.shape("turtle")
t.color(1,1,0)
t.bgcolor("black")
t.speed(8)

t.begin_fill()
for i in range(6):
    t.forward(10)
    t.right(60)
    t.forward(10)
    t.left(120)
t.end_fill()
t.ht()