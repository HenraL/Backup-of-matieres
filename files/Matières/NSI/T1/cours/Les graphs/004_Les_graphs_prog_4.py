# mon petit prog
from random import randint # on importe la lybrarie randint de random pour générer des nombres aléatoires
bin=[0,1] #on créé une liste comprise entre 0 et 1
length_of_line=randint(5,10) #on défini aléatoirement la longeur de la deuxième liste qui créé les lignes de la matrice
# list=[[bin[randint(0,1)]*length_of_line]*randint(5,10)] #j'ai tenté de créer la liste en une ligne mais je n'y suis pas arrivé

# Initialisation
list=[""]*randint(5,10) #on définit le nombre de lignes dans la liste
for i in range(len(list)): #on parcour les lignes de la liste
    k=[""]*length_of_line #on créé la liste k qui contiendras les valeurs de la ligne
    for K in range(len(k)): #on parcour k
        k[K]=bin[randint(0,len(bin)-1)] #pour chaque K dans k on remplace le "" par une valeur aléatoire entre 0 et 1
    list[i]=k #on écrase la ligne i de la liste avec la liste k
# list=[
#     [0, 1, 0, 0, 1, 0, 1, 1, 1],
#     [1, 0, 0, 1, 0, 1, 0, 1, 0],
#     [1, 1, 0, 0, 1, 0, 0, 1, 0],
#     [1, 1, 0, 0, 0, 1, 0, 0, 0],
#     [1, 0, 0, 0, 1, 1, 0, 0, 1],
#     [0, 1, 0, 0, 1, 1, 1, 1, 0],
#     [1, 0, 1, 1, 1, 0, 0, 0, 0],
#     [1, 1, 0, 0, 0, 1, 0, 0, 0],
#     [0, 1, 1, 1, 0, 0, 1, 0, 1]]

# Annalyse
print("Avec le booléen")
for line in range(len(list)): #on parcour les lignes de la liste
    for caracter in range(len(list[line])): #on parcour les caractères de la ligne définie par list[line]
        if list[line][caracter]==0: #si le caractère en question est 0 (ou null)
            print(False,end=",") # on écrit "False,"
        else: #sinon
            print(True,end=" ,") #on écrit "True,"
    print() # à chaque fin de ligne de la liste on ajoute une nouvelle ligne via print()
print() #à la fin de l'annalyse on met un retour à la ligne


print("Fini") #on écrit fini
print(list) #on affiche la liste d'origine

print("Avec le binaire")
#autre méthode d'affichage avec 0 et 1
for line in range(len(list)): #on parcour les lignes de la liste
    for caracter in range(len(list[line])): #on parcour les caractères de la ligne définie par list[line]
        if list[line][caracter]==0: #si le caractère en question est 0 (ou null)
            print(0,end=",") # on écrit "0,"
        else: #sinon
            print(1,end=",") #on écrit "1,"
    print() # à chaque fin de ligne de la liste on ajoute une nouvelle ligne via print()
print() #à la fin de l'annalyse on met un retour à la ligne

#autre méthode d'affichage
print("Avec None et 1")
for line in range(len(list)): #on parcour les lignes de la liste
    for caracter in range(len(list[line])): #on parcour les caractères de la ligne définie par list[line]
        if list[line][caracter]==0: #si le caractère en question est 0 (ou null)
            print(None,end=",") # on écrit "None,"
        else: #sinon
            print(1,end="   ,") #on écrit "1   ,"
    print() # à chaque fin de ligne de la liste on ajoute une nouvelle ligne via print()
print() #à la fin de l'annalyse on met un retour à la ligne



# [[0, 1, 0, 0, 1, 0, 1, 1, 1],
#  [1, 0, 0, 1, 0, 1, 0, 1, 0],
#  [1, 1, 0, 0, 1, 0, 0, 1, 0],
#  [1, 1, 0, 0, 0, 1, 0, 0, 0],
#  [1, 0, 0, 0, 1, 1, 0, 0, 1],
#  [0, 1, 0, 0, 1, 1, 1, 1, 0],
#  [1, 0, 1, 1, 1, 0, 0, 0, 0],
#  [1, 1, 0, 0, 0, 1, 0, 0, 0],
#  [0, 1, 1, 1, 0, 0, 1, 0, 1]]

# Voici le résultat d'affichage pour la liste 
"""
False,False,False,False,True ,True ,True ,True ,
True ,True ,True ,True ,True ,False,True ,True ,
True ,True ,False,True ,False,False,True ,False,
True ,True ,False,True ,False,True ,False,True ,
False,False,False,True ,True ,False,False,False,
False,False,True ,True ,False,True ,False,False,
False,True ,True ,False,False,True ,True ,False,
"""
"""Fini"""

"""list=[[0, 1, 0, 0, 1, 0, 1, 1, 1], [1, 0, 0, 1, 0, 1, 0, 1, 0], [1, 1, 0, 0, 1, 0, 0, 1, 0], [1, 1, 0, 0, 0, 1, 0, 0, 0], [1, 0, 0, 0, 1, 1, 0, 0, 1], [0, 1, 0, 0, 1, 1, 1, 1, 0], [1, 0, 1, 1, 1, 0, 0, 0, 0], [1, 1, 0, 0, 0, 1, 0, 0, 0], [0, 1, 1, 1, 0, 0, 1, 0, 1]]"""
"""
0,1,0,0,1,0,1,1,1,
1,0,0,1,0,1,0,1,0,
1,1,0,0,1,0,0,1,0,
1,1,0,0,0,1,0,0,0,
1,0,0,0,1,1,0,0,1,
0,1,0,0,1,1,1,1,0,
1,0,1,1,1,0,0,0,0,
1,1,0,0,0,1,0,0,0,
0,1,1,1,0,0,1,0,1,
"""

"""
None,1   ,None,None,1   ,None,1   ,1   ,1   ,
1   ,None,None,1   ,None,1   ,None,1   ,None,
1   ,1   ,None,None,1   ,None,None,1   ,None,
1   ,1   ,None,None,None,1   ,None,None,None,
1   ,None,None,None,1   ,1   ,None,None,1   ,
None,1   ,None,None,1   ,1   ,1   ,1   ,None,
1   ,None,1   ,1   ,1   ,None,None,None,None,
1   ,1   ,None,None,None,1   ,None,None,None,
None,1   ,1   ,1   ,None,None,1   ,None,1   ,
"""