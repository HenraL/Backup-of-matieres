firstlist=[]
listchecked=[]
listdisplay=[]
counter={}
cont="y"
while cont=="y":
    ask=input("Entrez n pour quiter (ou dérouler le programe(une fois les valeurs entrées)) ou o pour ovrir un fichier contenant une matrice ou un hexadécimal:").upper()
    if ask=="O":
        fto=input("entrez le nom exacte du fichier à ouvrir:")
        try:
            #print(fto)
            f=open(str(fto),"r")
            c=f.read()
            #print("c=",c)
            f.close()
            word=""
            for i in c:
                #print(i)
                if i==" " or i=="\n":
                    firstlist.append(word)
                    word=""
                else:
                    word+=str(i)
            cont="n"
        except:
            print("Désolé, une erreur est survenue dans le processus.\nVeuillez manuellement entrer les hexa")
    elif ask!="N":
        firstlist.append(str(ask))
    else:
        cont=ask
print("Ce que vous avez entré est: {}".format(firstlist))
for i in range(len(firstlist)):
    if firstlist[i] not in counter:
        counter[str(firstlist[i])]=1
    else:
        print("{} already in firstlist.".format(firstlist[i]))
        counter[str(firstlist[i])]+=1
for i in counter:
    if counter[i]>1:
        listdisplay.append(str(i))
    else:
        print("{} only one of a kind.".format(str(i)))
print("Les {} itérations sont: ".format(len(listdisplay)),end="")
for i in range(len(listdisplay)):
    if i==len(listdisplay)-1:
        print("{}".format(listdisplay[i]),end="")
    else:
        print("{}, ".format(listdisplay[i]),end="")
print(".")
print("L'élément apparaissant 5 fois est: ",end="")
for i in counter:
    if counter[i]==5:
        print("'{}'".format(i),end="")
print(".")
def pause():
    pause=input("Press enter to continue...")
pause()
pause()
pause()
pause()
