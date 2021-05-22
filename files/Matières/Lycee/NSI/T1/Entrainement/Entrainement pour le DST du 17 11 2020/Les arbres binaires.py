from binarytree import*
import datetime
date=datetime.datetime.now()
def pause():pause=input("press enter to continue...")
def prause(string):
    print(string)
    pause()
def writer(filename,auth,string):
        f=open(filename,auth)
        f.write(string)
        f.close()
class BI:
    def __init__(self):
        self.e=""
        self.runprog1=1
        self.runprog2=1
        self.runprog3=1
        self.Date="{}/{}/{}".format(date.day,date.month,date.year)
        self.DateFile="{} {} {} {} {} {}".format(date.day,date.month,date.year,date.hour,date.minute, date.second)
        # pour fibo2
        self.t=[0]*8
    def prog_1(self):
        current_prog="prog1"
        arbre1=tree()
        print(arbre1) #créer un arbre aléatoire
        writer("abre1 {} {} {}.txt".format(current_prog,self.DateFile,self.runprog1),"w","Random Binary Tree\n{}\n".format(arbre1))
        print(arbre1.preorder) #affichage préfixé
        writer("abre1 {} {} {}.txt".format(current_prog,self.DateFile,self.runprog1),"a","Affichage Préfixé\n{}\n".format(arbre1.preorder))
        print(arbre1.inorder) #affichage infixé
        writer("abre1 {} {} {}.txt".format(current_prog,self.DateFile,self.runprog1),"a","Affichage infixé\n{}\n".format(arbre1.inorder))
        print(arbre1.postorder) #affichage postfixé
        writer("abre1 {} {} {}.txt".format(current_prog,self.DateFile,self.runprog1),"a","Affichage postfixé\n{}\n".format(arbre1.postorder))
        self.runprog1+=1
    def prog_2(self):
        current_prog="prog2"
        arbre1=tree()
        print(arbre1) #créer un arbre aléatoire
        writer("abre1 {} {} {}.txt".format(current_prog,self.DateFile,self.runprog2),"w","Random Binary Tree\n{}\n".format(arbre1))
        print(arbre1.preorder) #affichage préfixé
        writer("abre1 {} {} {}.txt".format(current_prog,self.DateFile,self.runprog2),"a","Affichage Préfixé\n{}\n".format(arbre1.preorder))
        print(arbre1.inorder) #affichage infixé
        writer("abre1 {} {} {}.txt".format(current_prog,self.DateFile,self.runprog2),"a","Affichage infixé\n{}\n".format(arbre1.inorder))
        print(arbre1.postorder) #affichage postfixé
        writer("abre1 {} {} {}.txt".format(current_prog,self.DateFile,self.runprog2),"a","Affichage postfixé\n{}\n".format(arbre1.postorder))
        # arbre complet
        arbre2=heap(height=4, is_perfect=True)
        print(arbre2) #
        writer("abre2 {} {} {}.txt".format(current_prog,self.DateFile,self.runprog2),"a","Arbre 2\nheight=4, is_perfect=True\n{}\n".format(arbre2))
        arbre2=heap(height=4, is_perfect=False)
        print(arbre2) #
        writer("abre2 {} {} {}.txt".format(current_prog,self.DateFile,self.runprog2),"a","Arbre 2\nheight=4,is_perfect=False\n{}\n".format(arbre2))
        arbre2=heap(height=2, is_perfect=True)
        print(arbre2) #
        writer("abre2 {} {} {}.txt".format(current_prog,self.DateFile,self.runprog2),"a","Arbre 2\nheight=2, is_perfect=True\n{}\n".format(arbre2))
        arbre2=heap(height=2, is_perfect=False)
        print(arbre2) #
        writer("abre2 {} {} {}.txt".format(current_prog,self.DateFile,self.runprog2),"a","Arbre 2\nheight=2,is_perfect=False\n{}\n".format(arbre2))
        arbre2=heap(height=1, is_perfect=True)
        print(arbre2) #
        writer("abre2 {} {} {}.txt".format(current_prog,self.DateFile,self.runprog2),"a","Arbre 2\nheight=1, is_perfect=True\n{}\n".format(arbre2))
        arbre2=heap(height=1, is_perfect=False)
        print(arbre2) #
        writer("abre2 {} {} {}.txt".format(current_prog,self.DateFile,self.runprog2),"a","Arbre 2\nheight=1,is_perfect=False\n{}\n".format(arbre2))
        arbre2=heap(height=9, is_perfect=True)
        print(arbre2) #
        writer("abre2 {} {} {}.txt".format(current_prog,self.DateFile,self.runprog2),"a","Arbre 2\nheight=9, is_perfect=True\n{}\n".format(arbre2))
        arbre2=heap(height=9, is_perfect=False)
        print(arbre2) #
        writer("abre2 {} {} {}.txt".format(current_prog,self.DateFile,self.runprog2),"a","Arbre 2\nheight=9,is_perfect=False\n{}\n".format(arbre2))
        self.runprog2+=1
    def prog_3(self):
        current_prog="prog3"
        # construction d'un arbre
        racine=Node(1)
        racine.left=Node(2)
        racine.right=Node(3)
        racine.left.right=Node(4)
        print(racine)
        writer("abre3 {} {} {}.txt".format(current_prog,self.DateFile,self.runprog3),"a","Arbre 3\nracine={}\nracine.left={}\nracine.right={}\nracine.left.right={}".format(racine,racine.left,racine.right,racine.left.right))
        self.runprog3+=1
    def prog_4(self):
        def visite(arbre):
            if arbre==None:return 0
            print(arbre.value,end=" ")
            visite(arbre.left)
            visite(arbre.right)
        racine=Node(1)
        racine.left=Node(2)
        racine.right=Node(3)
        racine.left.right=Node(4)
        racine.left.right.right=Node(5)
        racine.left.right.left=Node(6)
        print(racine)
        visite(racine)
    def prog_5(self):
        def visite(arbre):
            if arbre==None:
                return 0
            visite(arbre.left)
            print(arbre.value,end=" ")
            visite(arbre.right)
        racine=Node(1)
        racine.left=Node(2)
        racine.right=Node(3)
        racine.left.right=Node(4)
        racine.left.right.right=Node(5)
        racine.left.right.left=Node(6)
        print(racine)
        visite(racine)
    def prog_6(self):
        def visite(arbre):
            if arbre==None:return 0
            visite(arbre.left)
            visite(arbre.right)
            print(arbre.value,end=" ")
        racine=Node(1)
        racine.left=Node(2)
        racine.right=Node(3)
        racine.left.right=Node(4)
        racine.left.right.right=Node(5)
        racine.left.right.left=Node(6)
        print(racine)
        visite(racine)
    def hauteur(arbre):
        if arbre==None:
            return 0
        return max(1+hauteur(arbre.left),1+hauteur(arbre.right))
    def fibo(n):
        if n==0 or n==1:return n
        else:
            print(BI.fibo(n-1)+BI.fibo(n-2))
            return BI.fibo(n-1)+BI.fibo(n-2)
    def fibod(n):
        # fist=[0]*n
        # c=0
        N1=[0]
        N2=[0]
        while n=>0:
            if n==0 or n==1:
                return n
            else:
                if n not in N1 and n not in N2:
                    n1=(n-1)
                    N1.append(n1)
                    n2=(n-2)
                    N2.append(n2)
                    n=n1+n2
                    print(n)
                    return (fibod(n-1)+fibod(n-2))
                else:
                    return n
                # return n
                # for i in range(len(fist)):
                    # if c==fist[i]:continue
                    # else:
                        # c=(n-1)+(n-2)
                        # print(c)
                        # fist.append(n)
        return n
                        
            
    def fibo2(n,self):
        print(self.t)
        print(n)
        if n==0 or n==1:
            self.t[n]=n
            return n
        if self.t[n]>0:
            return t[n]
        self.t[n]=fibo2(n-1)+fibo2(n-2)
        print(self.t)
        return (self.t[n])
    def fibo2(n):
        print(t)
        print(n)
        if n==0 or n==1:
            t[n]=n
            return n
        if t[n]>0:
            return t[n]
        t[n]=BI.fibo2(n-1)+BI.fibo2(n-2)
        print(t)
        return (t[n])
    # print("resultat = ",fibo2(7))
    def fibo3(n,t,self):
        print(n)
        print(self.t)
        if n==0 or n==1:
            self.t[n]=n
            return n
        if self.t[n]>0:
            return self.t[n]
        self.t[n]=fibo3(n-1,self.t)+fibo3(n-2,self.t)
        print(self.t)
        return (self.t[n])
    # print("resultat = ",fibo3(7))

    def recursiveChange(S,X):
        if X==0:return 0
        else:
            mini=X+1
            for i in range(len(S)):
                if S[i]<=X:
                    nb=1+recursiveChange(S,X-S[i])
                    if nb<mini:
                        mini=nb

        return mini
    def recherche_naive(tab,val):
        for i in range(len(tab)):
            if tab[i]==val:
                return i
        return -1
    def val_for_recherche_naive():
        liste=[1,4,32,7,3,9]
        valeur=7
        print(BI.recherche_naive(liste,valeur))
    def tri_selection(tab):
        for i in range(len(tab)):
            #trouver le min
            min=i
            for j in range(i+1,len(tab)):
                if tab[min]>tab[j]:
                    min=j
            #permuter avec élément indice i
            tmp=tab[i]
            tab[i]=tab[min]
            tab[min]=tmp
        return tab
    def val_for_tri_selection():
        tab=[10,7,3,5,8]
        print(tri_selection(tab))
    def tri_insertion(tab):
        #parcours de 1 à longuer du tableau
        for i in range(1,len(tab)):
            k=tab[i]
            j=i-1

            #recherche emplacement à insérer
            while j>=0 and k<tab[j]:
                tab[j+1]=tab[j]
                j=j-1

            #insertion
            tab[j+1]=k
    def val_for_tri_insertion():
        liste=[98,22,15,32,2,74]
        BI.tri_insertion(liste)
        print(liste)

    def recherche_dichotomique(tab,val):
        gauche=0
        droite=len(tab)-1
        while gauche <= droite:
            milieu=(gauche+droite)//2
            if tab[milieu]==val:
                #on a trouvé val dans le tableau
                #à la position milieu
                return milieu
            elif tab[milieu]>val:
                #on cherche entre gauche et milieu
                droite=milieu-1
            else: #on a tab[milieu]<val
                #on cherche entre milieu +1 et droite
                gauche=milieu+1
        #on est sorti de la boucle sans trouver val
        return -1
    def val_for_recherche_dichotomique():
        Tab=[1,3,7,8,12,15,25,37,42]
        val=14
        print(BI.recherche_dichotomique(Tab,val))
        val=12
        print(BI.recherche_dichotomique(Tab,val))
    



    # S=[1,2,5,10,20]
    # print(recursiveChange(S,30))
    
    # def rendu_monaie_mem(P,X):
        # mem=[0]*(X+1)
        # return rendu_monnaie_mem_c(P,X,mem)

BIN=BI()
# cont=True
# while cont==True:
#     launch=input("1 prog_1  2 prog_2  3 prog_3\n-2 executer un certain nombre de fois\n-1 tout\n0 quitter\nIndex du prog à afficher:")
#     if launch=="1":
#         print("prog_1(BIN)")
#         BI.prog_1(BIN)
#     elif launch=="2":
#         print("prog_2(BIN)")
#         BI.prog_2(BIN)
#     elif launch=="3":
#         print("prog_3(BIN)")
#         BI.prog_3(BIN)
#     elif launch=="-1":
#         print("prog_1(BIN)")
#         BI.prog_1(BIN)
#         print("prog_2(BIN)")
#         BI.prog_2(BIN)
#         print("prog_3(BIN)")
#         BI.prog_3(BIN)
#     elif launch=="-2":
#         notgiven=1
#         while notgiven==1:
#             times=input("Entrez le nombre de fois que ce sera exécuté:")
#             try:
#                 times=int(times)
#                 times+=1
#                 notgiven=0
#                 neithergiven=1
#                 while neithergiven==1:
#                     what=input("1 prog_1  2 prog_2  3 prog_3\n-1 tout\n0 sortir\nEntrez le/les programe(s) qui seront/sera exécuté:")
#                     if what=="1":
#                         for e in range(1,times):
#                             print("prog_1(BIN)")
#                             BI.prog_1(BIN)
#                         neithergiven=0
#                     elif what=="2":
#                         for e in range(1,times):
#                             print("prog_2(BIN)")
#                             BI.prog_2(BIN)
#                         neithergiven=0
#                     elif what=="3":
#                         for e in range(1,times):
#                             print("prog_3(BIN)")
#                             BI.prog_3(BIN)
#                         neithergiven=0
#                     elif what=="-1":
#                         for e in range(1,times):
#                             print("prog_1(BIN)")
#                             BI.prog_1(BIN)
#                             print("prog_2(BIN)")
#                             BI.prog_2(BIN)
#                             print("prog_3(BIN)")
#                             BI.prog_3(BIN)
#                         neithergiven=0
#                     else:
#                         prause("Please enter an index")
#             except:
#                 prause("Please enter a number.")

#     elif launch=="0":
#         cont=False
#         # break
#     else:
#         prause("Please enter an index")
#         pause()

print(BI.fibo(7))
print("BI.fibod")
print(BI.fibod(7))
# print(BI.fibo2(7,([0]*8)))
