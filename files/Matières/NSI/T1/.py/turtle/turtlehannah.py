from turtle import *
from random import *
a=90
speed(0)
COLOR=['blue','green','yellow','orange','red','purple','magenta']
home()
color("Blue")
bgcolor("black")
left(21)
bk(100)
rt(50)
fd(50)
dot(20, "pink")
fd(50)
for i in range(300):
    fd(a)
    dot(20, COLOR[randint(0,6)])
    fd(a)
    left(90)
    a+=1
    
goto(0,0)
clear()
a=90
for i in range(300):
    fd(a)
    dot(20, COLOR[randint(0,6)])
    fd(a)
    left(90)
    a+=10

goto(0,0)
clear()
a=1
for i in range(300):
    fd(a)
    dot(20, COLOR[randint(0,6)])
    fd(a)
    left(90)
    a+=1
    

goto(0,0)
clear()
a=1
for i in range(300):
    fd(a)
    dot(20, COLOR[randint(0,6)])
    fd(a)
    left(90)
    a+=10
