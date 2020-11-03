

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

#    a b c d
M =[[0,1,1,0],  #a
    [0,0,1,1],  #b
    [0,0,0,0],  #c
    [0,0,0,0]]  #d

# 2ème façon de procéder:
# création du graph directement:
# tester ci-dessous puis complèter pour rajouter les liaisons entre B-->C et B--D



graphe=noeud("A",0,noeud("B",0,0,1,1),noeud("C",0,0,0,0),0)