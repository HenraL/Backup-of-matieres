# 
#  Réaliser un graph
# très simplement 
# a partir matrice adjacence
# 
# 1. Taille du graph est connu
# par exemple 4 noeuds

class noeud:
    def __init__(self,numero,a,b,c,d):
        self.etiquette=numero
        self.pointeur_voisin1=a
        self.pointeur_voisin2=b
        self.pointeur_voisin3=c
        self.pointeur_voisin4=d
        print("self.etiquette={}".format(self.etiquette))
        print("self.pointeur_voisin1={}".format(self.pointeur_voisin1))
        print("self.pointeur_voisin2={}".format(self.pointeur_voisin2))
        print("self.pointeur_voisin3={}".format(self.pointeur_voisin3))
        print("self.pointeur_voisin4={}".format(self.pointeur_voisin4))
        print()


# matrice d'ajacement orienté a->b b->c b->d

#      a b c d
# M =[[0,1,1,0],  #a
    # [0,0,1,1],  #b
    # [0,0,0,0],  #c
    # [0,0,0,0]]  #d

# je créé mes 4 noeuds non liés pour le moment

noeud_A=noeud("A",None,1,1,None)
noeud_B=noeud("B",None,None,1,1)
noeud_C=noeud("C",None,None,None,None)
noeud_D=noeud("D",None,None,None,None)

# liaison manuelle:
# (visualisez chaque nouvelle ligne sous python tutor)
noeud_A.pointeur_voisin2=noeud_B
noeud_A.pointeur_voisin3=noeud_C
noeud_B.pointeur_voisin3=noeud_C
noeud_B.pointeur_voisin4=noeud_D


print(noeud_A.pointeur_voisin2)
print(noeud_A.pointeur_voisin3)
print(noeud_B.pointeur_voisin3)
print(noeud_B.pointeur_voisin4)

#

