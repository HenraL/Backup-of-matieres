import os
a=os.listdir()
colum=0
for i in range(len(a)):
    print("{} {}\t".format(i,a[i]),end="")
    if colum==2:
        colum=0
        print()
    colum+=1

b=int(input("Entrez l'index du fichier à convertir en base de donnée:"))
c=a[b]
f=open(c,"r")
d=f.read()
f.close()

e=input("Entrez le symbole qui sépare les termes de leurs définitions:")
f=input("Entrez le symbole qui sépare les terme/définition:")
word=""
word2=""
temp=""
liste=[]
A=0
for i in d:
    if i==f and A==1:
        word2=temp
        liste.append({"term":word,"definition":word2})
        word=word2=""
        A=0
    elif i==e and A==0:
        word=temp
        A=1
    else:
        temp+=str(i)
