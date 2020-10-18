from turtle import *
def dessin(taille):
    up()
    goto(-taille//2,-taille)
    down()
    forward(taille)
    up()
    goto(-taille//2,taille)
    down()
    forward(taille)

def trace(taille):
    if taille>0:
        dessin(taille)
        trace(taille-10)

trace(200)
pause=input("appuyez sur entré pour continuer...")