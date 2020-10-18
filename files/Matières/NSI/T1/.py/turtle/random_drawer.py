from random import *
import turtle
from pygame import image
tt=turtle
SCREEN=tt
tt.title("Random Drawer")
FORWARD=RIGHT=RANDCOLOR=Size=0
turns=randint(100,1000)
#turns=100
RIGHT=90
COLOR=['blue','green','yellow','orange','red','purple','magenta']
MAXCOLOR=len(COLOR)
positive=[1,-1]
tt.bgcolor('black')
def Randomiser(FORWARD,RIGHT,RANDCOLOR,Size):
    #FORWARD=randint(5,100)
    RIGHT=randint(-360,360)
    RANDCOLOR=randint(0,len(COLOR)-1)
    Size=randint(1,100)
    return FORWARD, RIGHT, RANDCOLOR, Size
for i in range(turns):
    #Randomiser(FORWARD,RIGHT,RANDCOLOR,Size)
    tt.forward(randint(5,50))
    tt.right(RIGHT+1)#randint(-90,90)
    tt.color(COLOR[randint(0,MAXCOLOR-1)])
    tt.width(randint(1,5))#Size
    tt.speed(0)
    RIGHT=randint(0,90)
    RIGHT*=positive[randint(0,1)]

#image.save(SCREEN, "screenshot.jpeg")
