from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    print(abs(pos()))
    if abs(pos())<1:
        break
end_fill()
