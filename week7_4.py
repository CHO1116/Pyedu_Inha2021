import turtle as t

T_Go = 10
T_Speed = 3
T_Color = (1,1,0)
Bg_Color = 'black'

t.shape('turtle')

t.speed(T_Speed)
t.color(T_Color)
t.bgcolor(Bg_Color)

t.begin_fill()
for i in range(8):
    t.forward(T_Go)
    t.right(45)
    t.forward(T_Go)
    t.left(90)
t.right(120)
t.forward(100)

for i in range(12):
    t.forward(T_Go)
    t.left(30)
    t.forward(T_Go)
    t.right(60)
t.left(120)
t.forward(100)

for i in range(15):
    t.forward(T_Go)
    t.left(24)
    t.forward(T_Go)
    t.right(48)
t.left(120)
t.forward(100)

t.end_fill()
t.ht()