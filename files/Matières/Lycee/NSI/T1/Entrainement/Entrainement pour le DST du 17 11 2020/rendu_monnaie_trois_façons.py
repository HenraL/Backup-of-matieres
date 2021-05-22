from time import sleep
# def pause():pause=input("press enter to continue")
def pause():return ""
def prause(string):
    print(string)
    pause()
class RI:
    def __init__(self,money,s):
        self.pieces=money
        self.coins=[1,2,4,5,10,20,50,100,200,500,1000,2000,5000,10000,20000,50000]
        self.s=s
        self.r=0
    
    def pause():print("pause")#sleep(0.5)#pause=input("press enter to continue")
    def rendu_monnaie_naïf(pieces,s): #à voir comme un arbre de possibilités partant du chiffre initial
        """renvoie le nombre minimal de pièces pour faire la somme s avec le système pieces"""
        if s==0:
            return 0
        r=s #s=1+1+...+1 dans le pire des cas
        for p in pieces:
            if p<=s:
                print("mon init={}\npieces test={}".format(s,pieces[p]))#r={}\np={}\n|r,p,
                r=min(r,1+RI.rendu_monnaie_naïf(pieces,s-p))
            RI.pause()
        return r
    def rendu_monnaie_dynamique(self,s):
        """renvoie le nombre minimal de pièces pour faire la somme s avec le système de pièces"""
        nb=[0]*(s+1)
        for n in range(1,s+1):
            nb[n]=n #n=1+1+1+...+1 dans le pire des cas
            for p in self.coins:
                if p <=n:
                    print("nb[n]={}\nnb={}".format(nb[n],nb))
                    nb[n]=min(nb[n],1+nb[n-p])
        return nb[s]
    def rendu_monnaie_avec_solution(self,s):
        """renvoie une liste de minimale de pièces pour faire la somme s avec le système de pieces"""
        nb=[0]*(s+1)
        sol=[[]]*(s+1)
        for n in range(1,s+1):
            nb[n]=n
            sol[n]=[1]*n
            for p in self.coins:
                if p<=n and 1+nb[n-p]<nb[n]:
                    nb[n]=1+nb[n-p]
                    sol[n]=sol[n-p].copy()
                    sol[n].append(p)
                    print("sol={}\nnb={}".format(sol,nb))
        return sol[s]
    def aligne_sequence(self,s1,s2):
        """Le score du meilleur alignement de s1 et s2"""
        n1,n2=len(s1),len(s2)
        sc=[[0]*(n2+1) for _ in range(n1+1)]
        #première ligne et première colonne
        for i in range(1,n1+1):
            sc[i][0]=-i
        for j in range(1,n2+1):
            sc[0][j]=-j
        #le reste
        for i in range(1,n1+1):
            for j in range(1,n2+1):
                s=max(-1+sc[i-1][j],-1+sc[i][j-1])
                if s1[i-1]==s2[j-1]:
                    sc[i][j]=max(s,1+sc[i-1][j-1])
                else:
                    sc[i][j]=max(s,-1+sc[i-1][j-1])
                # print(s)
        print(sc[n1][n2])
        print(sc)
        for b in range(len(sc)):
            for f in range(len(sc[b])):
                length=len("{}".format(sc[b][f]))
                if length==1:
                    print("| {}".format(sc[b][f]),end=" ")
                else:
                    print("|{}".format(sc[b][f]),end=" ")
            print("|")
        self.sc=sc
        return sc[n1][n2]
    def tester(self):
        print("self.sc[6][6]")
        print("self.sc[6][6]={}".format(self.sc[6][6]))
        print("max(1+self.sc[5][5],-1+self.sc[5][6],-1+self.sc[6][5])={}".format(max(1+self.sc[5][5],-1+self.sc[5][6],-1+self.sc[6][5])))
        print("self.sc[5][5]={},self.sc[5][6]={},self.sc[6][5]={}".format(self.sc[5][5],self.sc[5][6],self.sc[6][5]))
        print("self.sc[4][5]")
        print("self.sc[4][5]={}".format(self.sc[4][5]))
        print("max(1+self.sc[3][4],-1+self.sc[3][5],-1+self.sc[4][4])={}".format(max(1+self.sc[3][4],-1+self.sc[3][5],-1+self.sc[4][4])))
        print("self.sc[3][4]={},self.sc[3][5]={},self.sc[4][4]={}".format(self.sc[3][4],self.sc[3][5],self.sc[4][4]))
    def Ex_118():
        """ La réponse à l'exercice 118 """
        prause("rendu_monnaie_naïf(pieces,s) #Pour une liste de possibilité de pièces (Par exemple: [1,2]) et une somme initial à calculer (Par exemple:3)")
        prause("if s==0: #si la somme initiale est 0")
        prause("    return 0 #On retourne la valeur 0 car il n'y a rien à rendre")
        prause("r=s #s=1+1+...+1 dans le pire des cas #En revanche, si la valeur est non nul on attribut la valeur s à la variable r (si l'on reprends les valeurs dans l'exemple plus haut, r sera égal à 3)")
        prause("for p in pieces: #Pour chaque valeur dans la liste pieces (ici: [1,2]) on attribut l'une de ces valeur, au premier tour p sera égal à 1, au deuxième tour, p sera égal à 2.")
        prause("    if p<=s: #on vérifie que la somme à calculer est bien supérieur à la valeur choisie dans la liste.")
        prause("""        print("mon init={}\npieces test={}".format(s,pieces[p])) #ligne de debug, elles permettent d'afficher les calculs fait à chaque tour (elles ne font pas parties du programme initial)""")
        prause("        r=min(r,1+RI.rendu_monnaie_naïf(pieces,s-p)) #on initialise r avec la plus petite valeur de la récursive du programme, c'est-à-dire, la valeur actuelle de r et la definition actuelle avec la liste de peces et la somme initialle à laquelle on a soustrait la valeur à tester.")
        prause("    pause() # on freinne chaque boucle pour pouvoir suivre plus facillement le programe, encore une ligne rajouttée pour le debug.")
        prause("return r #on retourne le résultat final (r)")
        print("                L'arbre du résultat                      ")
        print("             _________________3_________________                 ")
        print("            / 3-1                           3-2 \                ")
        print("       ____2____                             ____1____           ")
        print("      / 2-1     \ 2-2                       / 1-1     \ 1-2      ")
        print("     1           0                         0          -1         ")
        print("    / 1-1                                                        ")
        prause("   0                                                             ")
    def Ex_119():
        """ La réponse de l'exercice 119 """
        prause("rendu_monnaie_dynamique(pieces,s) #Pour une liste de possibilité de pièces (Par exemple: [1,6,10]) et une somme initial à calculer (Par exemple:12)")
        prause("nb=[0]*(s+1) # on initialise la liste nb avec s+1 0.")
        prause("for n in range(1,s+1): #on boucle n fois s+1 en partant de 1, (au lieu de 0 en par défaut)")
        prause("    nb[n]=n #n=1+1+1+...+1 dans le pire des cas #on écrase la valeur n de la liste avec le résultat n")
        prause("    for p in pièces: #Pour chaque valeur dans la liste pieces (ici: [1,6,10]) on attribut l'une de ces valeur, au premier tour p sera égal à 1, au deuxième tour, p sera égal à 6, et au troisième tour, p sera égal à 10.")
        prause("        if p <=n: #on vérifie que la somme à calculer est bien supérieur à la valeur choisie dans la liste.")
        prause("""            print("nb[n]={}\nnb={}".format(nb[n],nb)) #ligne de debug, elles permettent d'afficher les calculs fait à chaque tour (elles ne font pas parties du programme initial)""")
        prause("            nb[n]=min(nb[n],1+nb[n-p]) #on écrase la valeur de la liste à la position n par la plus petite valeur du calcule 1+nb[n-p]")
        prause("return nb[s] #on retourne le résultat final nb[s]")
        prause("                L'arbre du résultat                      ")
        print("                                          ____________________________________________12____________________________________________                 ")
        print("                                         /12-1                                         |12-6                                        \12-6          ")
        print("                                     ____11____                                     ____6____                                    ____6____          ")
        print("                                    /11-1 |11-6 \11-10                             /6-1 |6-6 \6-10                              /6-1 |6-6 \6-10     ")
        print("                               ____5____  7     ___1___                       ____5____ 0    -4                            ____5____ 0    -4        ")
        print("                              /5-1 |5-6 \5-10  /1-1|1-6\1-10                 /5-1 |5-6 \5-10                              /5-1 |5-6 \5-10           ")
        print("                        ____4____ -1    -5    0   -4   -9              ____4____ -1    -5                           ____4____ -1    -5              ")
        print("                       /4-1 |4-6 \4-10                                /4-1 |4-6 \4-10                              /4-1 |4-6 \4-10                  ")
        print("                  ____3____-2    -6                              ____3____-2    -6                            ____3____-2    -6                     ")
        print("                 /3-1 |3-6 \3-10                                /3-1 |3-6 \3-10                              /3-1 |3-6 \3-10                        ")
        print("            ____2____ -3   -7                              ____2____ -3   -7                            ____2____ -3   -7                           ")
        print("           /2-1 |2-6 \2-10                                /2-1 |2-6 \2-10                              /2-1 |2-6 \2-10                              ")
        print("      ____1____ -4   -8                              ____1____ -4   -8                            ____1____ -4   -8                                 ")
        print("     /1-1 |1-6 \1-10                                /1-1 |1-6 \1-10                              /1-1 |1-6 \1-10                                    ")
        print("    0     -5    -9                                 0     -5    -9                               0     -5    -9                                      ")
        prause("option 6 finie, le reste est encore à faire.")
                 
                  
                  
                  
                  
                  
word1="ENORME"
word2="GENOME"

# money=[1,2,3,4,5,6,7,8,9,10,100]
# money.reverse()
money=[100, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
RIN=RI(money,10)
# money=[100,9,7,5,3,1,2,4,6,8,10]
# print("rendu_monnaie_naïf")
# print(RI.rendu_monnaie_naïf(money,10))
# print("rendu_monnaie_dynamique")
print(RI.rendu_monnaie_dynamique(RIN,10))
# print("rendu_monnaie_avec_solution")
# print(RI.rendu_monnaie_avec_solution(RIN,10))
print("aligne_sequence")
print(RI.aligne_sequence(RIN,word2,word1))#money,money
print("aligne_sequence")
print(RI.aligne_sequence(RIN,"GENO-ME","-ENORME"))#money,money
print("tester")
# print(RI.tester(RIN))
# RI.Ex_118()
# RI.Ex_119()
