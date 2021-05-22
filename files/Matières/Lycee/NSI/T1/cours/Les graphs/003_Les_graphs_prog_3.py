# 
# Construction noeud à n voisins (sommets)
# Construction du graphe automatiquement
# à partir de la matrice 
class noeud:
    def __init__(self,numero,liste_sommets):
        self.etiquette = numero
        self.nb_sommets=len(liste_sommets)
        self.liste_pointeur_voisins=[]
        for i in range(self.nb_sommets):
            self.liste_pointeur_voisins=self.liste_pointeur_voisins+[None]
        print(self.liste_pointeur_voisins)

M =[[0,1,1,0],
    [0,0,1,1],
    [0,0,0,0],
    [0,0,0,0]]



noeud_A=noeud("A",["A","B","C","D"])
noeud_B=noeud("B",["A","B","C","D"])
noeud_C=noeud("C",["A","B","C","D"])
noeud_D=noeud("D",["A","B","C","D"])

noeud_A.liste_pointeur_voisins[1]=noeud_B
noeud_B.liste_pointeur_voisins[2]=noeud_C
noeud_B.liste_pointeur_voisins[3]=noeud_D