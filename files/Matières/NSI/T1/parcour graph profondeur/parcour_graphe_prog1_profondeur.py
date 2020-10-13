class noeud:
    def __init__(self,numero,liste_sommets):
        self.etiquette=numero              #numero du sommet
        self.coleur="blanc"                #couleur arbitraire
        self.nb_sommets=len(liste_sommets) #nombre de sommets du graphe
        self.liste_pointeur_voisins=[]
    
    for i in range(self.nb_sommets):
        self.listepointeur_voisins = self.liste_pointeur_voisins+[None]
    
    print(self.listepointeur_voisins)

#matrice d'ajacence

#   a b c d e f g h i
M=[[0,1,1,1,0,0,0,0,0], #a
   [1,0,1,0,0,0,1,0,0], #b
   [1,1,0,0,1,1,0,0,0], #c
   [1,0,0,0,0,1,0,0,0], #d
   [0,0,1,0,0,0,1,1,1], #e
   [0,0,1,1,0,0,0,0,1], #f
   [0,1,0,0,1,0,0,0,0], #g
   [0,0,0,0,1,0,0,0,0], #h
   [0,0,0,0,1,1,0,0,0]] #i

#création du graphe avec la liste des sommets

sommets=["A","B","C","D","E","F","G","H","I"]
graphe=[noeud("A",sommets),noeud("B",sommets),noeud("C",sommets),noeud("D",sommets),noeud("E",sommets),noeud("F",sommets),noeud("G",sommets),noeud("H",sommets),noeud("I",sommets)]

#création des liaisons entre les sommets
for ligne in range(len(M)):
    for colonne in range(len(M)):
        if M[ligne][colonne]==1:
            graphe[ligne].liste_pointeur_voisins[colonne]=graphe[colonne]

#Algo parcous en profondeur (version récursive)

def parcours_profondeur(u):
    u.couleur="noir"
    print(u.etiquette, end=" ")
    for v in range(len(M)):
        if v!=None and v.couleur!="noir":
            parcours_profondeur(v)

u=graphe[0]            #noeud A
parcours_profondeur(u)




# https://www.eduscol.education.fr/cid144156/nsi-bac-2021.html
# https://www.pixees.fr/informatiquelycee/n_site/nsi_term_structDo_arbre