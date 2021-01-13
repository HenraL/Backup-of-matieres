#elementaries
def creer_pile_vide():
 e=[]
 return e

def empiler(list,elem):
 list.append(elem)
 return list

def depiler(list):
 return list.pop(0)

def est_vide(list):
 if len(list)==0:
  return True
 else:
  return False

#secondary elementaries q2
def hauteur_pile(P):
 Q=creer_pile_vide()
 n=0
 while not(est_vide(P)==True):
  n+=1
  empiler(Q,depiler(P))
 while not(est_vide(Q)==True):
  empiler(P,depiler(Q))
 return n

#code_pseudo q3
"""
def max_pile(P,i):
 Q=creer_pile_vide()
 index=0
 #F=0
 while not(est_vide(P)==True):
  if index==i:
   F=depiler(P)
   empiler(Q,F)
  else:
   empiler(Q,depiler(P))
  index+=1
 #empiler(P,F)
 while not(est_vide(Q)==True):
  empiler(P,depiler(Q))
 G=F
 return G
"""

"""def max_pile(P,i):
 S=0
 Q=creer_pile_vide()
 indice=0
 j=0
 max=0
 while S<i:
  empiler(Q,depiler(P))
  S+=1
 while not(est_vide(P)==True):
  F=depiler(P)
  if (F>=max):
   max=F
   indice=j
  empiler(Q,F)
  j+=1
 indice+=i
 while not(est_vide(Q)==True):
  empiler(P,depiler(Q))
 return indice"""

def max_pile(P,i):
    indice=0
    maxo=0
    j=0
    Q=creer_pile_vide()
    while j<=i:
        print("P(max_pile)=",P)
        F=depiler(P)
        if F>=maxo:
            maxo=F
            indice=j
        j+=1
        empiler(Q,F)
    while not(est_vide(Q)==True):
        empiler(P,depiler(Q))
    return indice

def retourner(P,j):
 assert j <= hauteur_pile(P), "La liste est vide"
 Q=creer_pile_vide()
 #R=creer_pile_vide()
 T=creer_pile_vide()
 rang=1#0
 while rang<=j:
  empiler(Q,depiler(P))
  rang+=1
 while not(est_vide(P)==True):
  empiler(T,depiler(P))
 long=hauteur_pile(Q)
 for i in range(long-1):
  empiler(Q,depiler(Q))
 while not(est_vide(Q)==True):
  empiler(P,depiler(Q))
 while not(est_vide(T)==True):
  empiler(P,depiler(T))
 return P#None

#code pour q5 M.OBELE
def tri_crepes(P):
    Q=creer_pile_vide()
    assert not(est_vide(P)), "Il n'y a pas de crêpes à trier"
    print(P)
    h=hauteur_pile(P)
    print(P)
    for i in range(0,h-1):
        print("P=",P)
        rang_maxi=max_pile(P,h-i-1)
        print("P(rang_maxi)=",P)
        retourner(P,rang_maxi)
        print("P(retourner)=",P)
        empiler(Q,depiler(P))
        print("P(depiler)=",P,"Q(empiler)=",Q)
    while not(est_vide(Q)==True):
        empiler(P,depiler(Q))
        print("Q=",Q," to P=",P)
    return None

P=[6,3,9,5]
tri_crepes(P)
