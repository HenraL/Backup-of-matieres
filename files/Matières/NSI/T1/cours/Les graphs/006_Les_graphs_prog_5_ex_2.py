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
        #print()


# matrice d'ajacement orienté a->b b->c b->d

#------>
#sens de lecture
# X    a b c d     Y
# M =[[0,1,1,0],  #a
    # [0,0,1,1],  #b
    # [0,0,0,0],  #c
    # [0,0,0,0]]  #d

# je créé mes 4 noeuds non liés pour le moment
#X                        Y
graphe=noeud("A",0,noeud("B",1,0,0,0),noeud("C",1,1,0,0),0)
#noeud_A=noeud("A",0,0,0,0)
#noeud_B=noeud("B",1,0,0,0)
#noeud_C=noeud("C",1,1,0,0)
#noeud_D=noeud("D",0,1,0,0)
# liaison manuelle:
# (visualisez chaque nouvelle ligne sous python tutor)
#noeud_A.pointeur_voisin2=noeud_B.pointeur_voisin2
#noeud_A.pointeur_voisin3=noeud_C.pointeur_voisin3
#noeud_B.pointeur_voisin3=noeud_C.pointeur_voisin3
#noeud_B.pointeur_voisin4=noeud_D.pointeur_voisin1


graphe2=noeud("A","A1",noeud("B","B1","B2","B3","B4"),noeud("C","C1","C2","C3","C4"),"A4")
# liaison manuelle:
# (visualisez chaque nouvelle ligne sous python tutor)
#noeud_AA.pointeur_voisin2=noeud_BB.pointeur_voisin2
#noeud_AA.pointeur_voisin3=noeud_CC.pointeur_voisin3
#noeud_BB.pointeur_voisin3=noeud_CC.pointeur_voisin3
#noeud_BB.pointeur_voisin4=noeud_DD.pointeur_voisin1
"""noeud_A=noeud("A",11,12,13,14)
noeud_B=noeud("B",21,22,23,24)
noeud_C=noeud("C",31,32,33,34)
noeud_D=noeud("D",41,42,43,44)"""

print("XY")
print("  A B C D")
print("A",graphe.pointeur_voisin1,graphe.pointeur_voisin1,graphe.pointeur_voisin1)#,noeud_D.pointeur_voisin1)
print("B",graphe.pointeur_voisin2.pointeur_voisin2,graphe.pointeur_voisin2.pointeur_voisin3,graphe.pointeur_voisin2)#,noeud_D.pointeur_voisin2)
print("C",graphe.pointeur_voisin3.pointeur_voisin3,graphe.pointeur_voisin3,graphe.pointeur_voisin3)#,noeud_D.pointeur_voisin3)
print("D",graphe.pointeur_voisin4,graphe.pointeur_voisin4,graphe.pointeur_voisin4)#,noeud_D.pointeur_voisin4)
#print("XY")
#print("  A B C D")
#print("A",noeud_A.pointeur_voisin1,noeud_B.pointeur_voisin1,noeud_C.pointeur_voisin1,noeud_D.pointeur_voisin1)
#print("B",noeud_A.pointeur_voisin2,noeud_B.pointeur_voisin2,noeud_C.pointeur_voisin2,noeud_D.pointeur_voisin2)
#print("C",noeud_A.pointeur_voisin3,noeud_B.pointeur_voisin3,noeud_C.pointeur_voisin3,noeud_D.pointeur_voisin3)
#print("D",noeud_A.pointeur_voisin4,noeud_B.pointeur_voisin4,noeud_C.pointeur_voisin4,noeud_D.pointeur_voisin4)
print("XY")
print("  A B C D")
print("A",graphe2.noeud_AA.pointeur_voisin1,graphe2.noeud_BB.pointeur_voisin1,graphe2.noeud_CC.pointeur_voisin1)#,noeud_DD.pointeur_voisin1)
print("B",graphe2.noeud_AA.pointeur_voisin2,graphe2.noeud_BB.pointeur_voisin2,graphe2.noeud_CC.pointeur_voisin2)#,noeud_DD.pointeur_voisin2)
print("C",graphe2.noeud_AA.pointeur_voisin3,graphe2.noeud_BB.pointeur_voisin3,graphe2.noeud_CC.pointeur_voisin3)#,noeud_DD.pointeur_voisin3)
print("D",graphe2.noeud_AA.pointeur_voisin4,graphe2.noeud_BB.pointeur_voisin4,graphe2.noeud_CC.pointeur_voisin4)#,noeud_DD.pointeur_voisin4)
print("YX")
print("  A B C D")
print("A",graphe.noeud_A.pointeur_voisin1,graphe.noeud_A.pointeur_voisin2,graphe.noeud_A.pointeur_voisin3,graphe.noeud_A.pointeur_voisin4)
print("B",graphe.noeud_B.pointeur_voisin1,graphe.noeud_B.pointeur_voisin2,graphe.noeud_B.pointeur_voisin3,graphe.noeud_B.pointeur_voisin4)
print("C",graphe.noeud_C.pointeur_voisin1,graphe.noeud_C.pointeur_voisin2,graphe.noeud_C.pointeur_voisin3,graphe.noeud_C.pointeur_voisin4)
#print("D",noeud_D.pointeur_voisin1,noeud_D.pointeur_voisin2,noeud_D.pointeur_voisin3,noeud_D.pointeur_voisin4)
print("YX")
print("  A B C D")
print("A",graphe2.noeud_AA.pointeur_voisin1,graphe2.noeud_AA.pointeur_voisin2,graphe2.noeud_AA.pointeur_voisin3,graphe2.noeud_AA.pointeur_voisin4)
print("B",graphe2.noeud_BB.pointeur_voisin1,graphe2.noeud_BB.pointeur_voisin2,graphe2.noeud_BB.pointeur_voisin3,graphe2.noeud_BB.pointeur_voisin4)
print("C",graphe2.noeud_CC.pointeur_voisin1,graphe2.noeud_CC.pointeur_voisin2,graphe2.noeud_CC.pointeur_voisin3,graphe2.noeud_CC.pointeur_voisin4)
#print("D",noeud_DD.pointeur_voisin1,noeud_DD.pointeur_voisin2,noeud_DD.pointeur_voisin3,noeud_DD.pointeur_voisin4)

"""print(noeud_A.pointeur_voisin2)
print(noeud_A.pointeur_voisin3)
print(noeud_B.pointeur_voisin3)
print(noeud_B.pointeur_voisin4)

#"""

