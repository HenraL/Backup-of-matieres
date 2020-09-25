from random import *
from turtle import *
def puissance(x,n):
    if n==0:
        x=1
        return x
    elif n>0:
        print(x," ",n)
        x=x*(x*puissance(x,n-1))
        return x

print(puissance(10,100))

def isertion(list, x, n):
    if n>0:
        list[n-1]=x
        return list, x, n
    else: isertion(list, list[randint(0,len(list))], randint(0,len(list)))

list=[]
for i in range(randint(0,randint(100,200))):list.append(randint(randint(-200,0),randint(100,200)))
# print(list)
x=list[randint(0,len(list))]
n=randint(0,len(list))
print(x," ",n)
isertion(list, x, n)
print(x)
print(n)
print(list)

def tri_insertion(list,liste_triee):
    for i in list:
        elementATrier=i
        for I in range(len(liste_triee)):
            if elementATrier<list[I]:
                liste_triee[I].append(elementATrier)
            elif elementATrier==list[I]:
                liste_triee[I].append(elementATrier)
            elif elementATrier>list[I]:
                liste_triee[I+1].append(elementATrier)
    return liste_triee

liste_triee=[]
list=[]
for i in range(randint(0,randint(100,200))):list.append(randint(randint(-200,0),randint(100,200)))
print(tri_insertion(list,liste_triee))

couleurs=['blue','green','yellow','orange','red','purple']
bgcolor('black')
def dessin(tours):
    if tours!=180:
        color(couleurs[tours%6])
        forward(tours)
        right(59)
        dessin(tours+1)
        print(tours)
    else:
        return tours
tours=0
dessin(tours)

# for i in range(180)