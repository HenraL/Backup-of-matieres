from random import *
from turtle import *
from math import *
from time import sleep
ma_liste=[1,4,7,8,9,27,28,30,32,99,105,110,115,200,210,220]
#
# Recherche dichotomique
# version itérative
#

# espace Turing machine de turing
#the little man computer
turtley=[]
turtlex=[]
def recherche_dichotomique(tab,val):
    gauche=0
    droite=len(tab)-1
    while gauche <= droite:
        milieu=(gauche+droite)//2
        if tab[milieu]==val: #on a trouvé
            print("tab[milieu]={}".format(tab[milieu]))
            turtley.append(log(tab[milieu]))
            turtlex.append(tab[milieu])
            return milieu,turtley,turtlex
        elif tab[milieu]>val:
            droite=milieu-1
            print("tab[milieu]={}".format(tab[milieu]))
        else:
            gauche=milieu+1
            print("tab[milieu]={}".format(tab[milieu]))
    return -1

ma_liste=[]
RANDOM=False#True
if RANDOM==True:
    for i in range(randint(0,randint(5000,6000))):
        ma_liste.append(randint(0,6000))
else:
    ma_liste=list(range(6000))
print(ma_liste)
val=5000
print("recherche de {}".format(val))
resultat=recherche_dichotomique(ma_liste,val)
print("Position = {}".format(resultat))

for i in range(len(turtley)):
    goto(turtlex[i],turtley[i])

print(turtley)
print(turtlex)

sleep(5)