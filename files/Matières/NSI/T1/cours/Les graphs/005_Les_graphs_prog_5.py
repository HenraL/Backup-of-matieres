# """un graphe représenté par une matrice d'adjacence, où les sommets sont les entiers 0,1,...,n-1"""
from random import randint
n = 20
bool = [True, False]
class Graphe:
    def __init__(self,n):
        self.n = n
        self.adj = [[False]*n for _ in range(n)]

    def ajouter_arc(self,s1,s2):
        self.adj[s1][s2] = True
    def arc(self,s1,s2):
        return self.adj[s1][s2]

    def voisins(self, s):
        v = []
        for i in range(self.n):
            if self.adj[s][i]:
                v.append(i)
        return v
    # def afficher(self):
    #     for i in range(randint(0,len(self.adj[len(self.adj)][len(self.adj[len(self.adj)])]))):
    #         s1 = i
    #         s2 = randint(0,len(self.adj[s1]))
    #         Graphe.ajouter_arc(self,s1,s2)
    #     for s in range(self.adj):
    #         for v in range(len(self.adj[s])):
    #             print(self.adj[s][v],end = ",")
    #         print()
    #     Graphe.voisins()
    # def lambda():
        Graphe.afficher(self)


# Graphe.lambda()