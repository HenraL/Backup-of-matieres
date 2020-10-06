ma_liste=[1,4,7,8,9,27,28,30,32,99,105,110,115,200,210,220]
#
# Recherche dichotomique
# version itérative
#

# espace Turing machine de turing
#the little man computer

def recherche_dichotomique(tab,val):
    gauche=0
    droite=len(tab)-1
    while gauche <= droite:
        milieu=(gauche+droite)//2
        if tab[milieu]==val: #on a trouvé
            print("tab[milieu]={}".format(tab[milieu]))
            return milieu
        elif tab[milieu]>val:
            droite=milieu-1
            print("tab[milieu]={}".format(tab[milieu]))
        else:
            gauche=milieu+1
            print("tab[milieu]={}".format(tab[milieu]))
    return -1

ma_liste=[1,4,7,8,9,27,28,30,32,99,105,110,115,200,210,220]
val=16
print("recherche de {}".format(val))
resultat=recherche_dichotomique(ma_liste,val)
print("Position = {}".format(resultat))