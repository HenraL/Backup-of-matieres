ma_liste=[1,4,7,8,9,27,28,30,32,99,105,110,115,200,210,220]
#1-Solution Naive
# Parcours linéaire
def recherche_naive(T,x):
    for i in range(len(T)):
        if T[i]==x:
            return i
        if T[i]>x: #pas la peine d'aller chercher plus loin
            return -1
    return -1

print(recherche_naive(ma_liste,27))