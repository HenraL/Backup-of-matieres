def fact_term(n,acc): #on définit le nombre d'itération grâce à la variable n, on définit acc qui prendra la valeur de n*acc.
    if n>0: #on vérifie que l'on n'as épuisé le nombre d'itérations, tant que n est supérieur à 0 on continue l'ittération.
        return fact_term(n-1,acc*n)#on renvoie la valeur d'accc*n et on décréme te n.
    else: # Si n a atein 0, c'est à dire le nombre maximal de tours, on se contente de renvoyer la valeur d'acc.
        return acc # On renvoie la valeur d'acc.

print("fact_term(5,5)={}".format(fact_term(5,5))) #On afffiche le résultat de la fonction n,acc.

""" le premier terme de la fonction sert à définir le nombre de fois que la boucle va être itérée
    le premier terme 'n' sert aussi à définir le deuxième terme du produit de n*acc
    le deuxième terme 'acc' est un accumulateur car à chaque itération de la boucle
    il prendra la valeur de acc*n"""

print("fact_term(5,4)={}".format(fact_term(5,4)))
print("fact_term(5,3)={}".format(fact_term(5,3)))
print("fact_term(5,2)={}".format(fact_term(5,2)))
print("fact_term(5,1)={}".format(fact_term(5,1)))
print("fact_term(5,0)={}".format(fact_term(5,0)))

print("fact_term(4,5)={}".format(fact_term(4,5)))
print("fact_term(4,4)={}".format(fact_term(4,4)))
print("fact_term(4,3)={}".format(fact_term(4,3)))
print("fact_term(4,2)={}".format(fact_term(4,2)))
print("fact_term(4,1)={}".format(fact_term(4,1)))
print("fact_term(4,0)={}".format(fact_term(4,0)))

print("fact_term(3,5)={}".format(fact_term(3,5)))
print("fact_term(3,4)={}".format(fact_term(3,4)))
print("fact_term(3,3)={}".format(fact_term(3,3)))
print("fact_term(3,2)={}".format(fact_term(3,2)))
print("fact_term(3,1)={}".format(fact_term(3,1)))
print("fact_term(3,0)={}".format(fact_term(3,0)))

print("fact_term(2,5)={}".format(fact_term(2,5)))
print("fact_term(2,4)={}".format(fact_term(2,4)))
print("fact_term(2,3)={}".format(fact_term(2,3)))
print("fact_term(2,2)={}".format(fact_term(2,2)))
print("fact_term(2,1)={}".format(fact_term(2,1)))
print("fact_term(2,0)={}".format(fact_term(2,0)))

print("fact_term(1,5)={}".format(fact_term(1,5)))
print("fact_term(1,4)={}".format(fact_term(1,4)))
print("fact_term(1,3)={}".format(fact_term(1,3)))
print("fact_term(1,2)={}".format(fact_term(1,2)))
print("fact_term(1,1)={}".format(fact_term(1,1)))
print("fact_term(1,0)={}".format(fact_term(1,0)))

print("fact_term(0,5)={}".format(fact_term(0,5)))
print("fact_term(0,4)={}".format(fact_term(0,4)))
print("fact_term(0,3)={}".format(fact_term(0,3)))
print("fact_term(0,2)={}".format(fact_term(0,2)))
print("fact_term(0,1)={}".format(fact_term(0,1)))
print("fact_term(0,0)={}".format(fact_term(0,0)))