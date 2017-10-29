import turtle as t
import random

t.shape("turtle")
t.speed(0)
t.up()
t.goto(-100,-100)
t.down()
for x in range(4):
    t.fd(500)
    t.lt(90)
t.up()
t.goto(200,200)
t.down()
t.pos()
a=random.randint(1,360)
t.seth(a)


while True:
    while -100<t.xcor()<401 and -100<t.ycor()<401:
         t.fd(1)
         a=t.heading()
    while 400<=t.xcor()<=400:
        if 0<a<90:
            t.seth(180-a)
            t.fd(1)
        elif 270<a<360 :
            t.seth(540-a)
            t.fd(1)
    while -101<=t.xcor()<=-100:
        if 90<a<180:
            t.seth(180-a)
            t.fd(1)
        elif 180<a<270:
            t.seth(540-a)
            t.fd(1)
    while 400<=t.ycor()<401:
        if 0<a<180:
            t.seth(360-a)
            t.fd(1)
    while -100<t.ycor()<=-100:
        if 180<a<360:
            t.seth(360-a)
            t.fd(1)
