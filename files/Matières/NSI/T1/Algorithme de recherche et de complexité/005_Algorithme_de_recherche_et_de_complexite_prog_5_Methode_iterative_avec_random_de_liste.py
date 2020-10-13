from random import *
# from turtle import *
from math import *
from time import sleep
ma_liste=[1,4,7,8,9,27,28,30,32,99,105,110,115,200,210,220]
#
# Recherche dichotomique
# version itérative
#

# espace Turing machine de turing
#the little man computer

def recherche_dichotomique(T,x,gauche,droite):
    milieu=(gauche+droite)//2
    if gauche>droite:
        return -1
    if x==T[milieu]:
        return milieu
    if x>T[milieu]:
        return recherche_dichotomique(T,x,milieu+1,droite) #Je cherche entre milieu+1 et droite
    else:
        return recherche_dichotomique(T,x,gauche,milieu-1) #Je cherche entre gauche et milieu-1

# def recherche_dicho(T,x):
#     return recherche_dichotomique(T,x,0,len(T)-1)


ma_liste=[]
RANDOM=False#True
DEFAULTLIST=True
if RANDOM==True:
    for i in range(randint(0,randint(5000,6000))):
        ma_liste.append(randint(0,6000))
else:
    if DEFAULTLIST==True:
        ma_liste=[1,4,7,8,9,27,28,30,32,99,105,110,115,200,210,220]
    else:
        ma_liste=list(range(6000))
print(ma_liste)
val=115
print("recherche de {}".format(val))
resultat=recherche_dichotomique(ma_liste,val,0,len(ma_liste)-1)#recherche_dicho(ma_liste,val)
print("Position = {}".format(resultat))

# sleep(5)