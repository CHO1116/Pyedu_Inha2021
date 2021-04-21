import turtle as t

T_Go = 10
T_Speed = 8
T_Color = (1,1,0)
Bg_Color = 'black'

t.shape('turtle')

t.speed(T_Speed)
t.color(T_Color)
t.bgcolor(Bg_Color)

t.begin_fill()
for i in range(6):
    t.forward(T_Go)
    t.right(60)
    t.forward(T_Go)
    t.left(120)
t.end_fill()

t.ht()