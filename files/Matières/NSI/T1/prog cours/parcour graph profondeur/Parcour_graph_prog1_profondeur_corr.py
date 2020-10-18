class noeud:
    def __init__(self,numero,liste_sommets):
        self.etiquette=numero              #numero du sommet
        self.couleur="blanc"                #couleur arbitraire
        self.nb_sommets=len(liste_sommets) #nombre de sommets du graphe
        self.liste_pointeur_voisins=[]

        for i in range(self.nb_sommets):
            self.liste_pointeur_voisins = self.liste_pointeur_voisins + [None]
            print(self.liste_pointeur_voisins)
            # print(M)
            # print(self.nb_sommets)
            print(i)

#   A B C D E F G H I
M=[[0,1,1,1,0,0,0,0,0], #A
   [1,0,1,0,0,0,1,0,0], #B
   [1,1,0,0,1,1,0,0,0], #C
   [1,0,0,0,0,1,0,0,0], #D
   [0,0,1,0,0,0,1,1,1], #E
   [0,0,1,1,0,0,0,0,1], #F
   [0,1,0,0,1,0,0,0,0], #G
   [0,0,0,0,1,0,0,0,0], #H
   [0,0,0,0,1,1,0,0,0]] #I

#création du graphe avec la liste des sommets

sommets=["A","B","C","D","E","F","G","H","I"]
graphe=[noeud("A",sommets),noeud("B",sommets),noeud("C",sommets),noeud("D",sommets),
noeud("E",sommets),noeud("F",sommets),noeud("G",sommets),noeud("H",sommets),noeud("I",sommets)]
# print(graphe)

#création des liaisons entre les sommets
for ligne in range(len(M)):
    for colonne in range(len(M)):
        if M[ligne][colonne] == 1:
            graphe[ligne].liste_pointeur_voisins[colonne]=graphe[colonne]
            # print(graphe)
            # print(graphe[ligne].liste_pointeur_voisins)

#Algo parcous en profondeur (version récursive)

def parcours_profondeur(u):
    u.couleur="noir"
    print(u.etiquette, end=" ")
    for v in u.liste_pointeur_voisins:
        if v!=None and v.couleur!="noir":
            parcours_profondeur(v)
            # print(u.couleur)
            # print(v)

u=graphe[0]            #noeud A
# print(u)
# print(graphe[0])
parcours_profondeur(u)

"""Le programme parcour les lignes de la matrice et retourne les lettres qui ont pour comme point commun la même lettre"""