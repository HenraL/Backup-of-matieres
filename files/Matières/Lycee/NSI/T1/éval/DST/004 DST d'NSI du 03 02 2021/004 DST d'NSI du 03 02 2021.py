class Tot:
    def __init__(self):
        self.pic=0
class pb1q1(Tot):
    def pyramide_inversee(n):
        print(TI.pic,' '*(20-n)+'*'*(2*n+1),n)
        TI.pic+=1
        Tot.pyramide_inversee(n-1)
    def pyramide_inversee_rep(n):
        print(TI.pic,' '*(20-n)+'*'*(2*n+1))
        TI.pic+=1
        if n>0:
            Tot.pyramide_inversee_rep(n-1)
class pb1q2(Tot):
    def saute(troupeau1:list, troupeau2:list):
        mouton=troupeau1.pop()
        troupeau2.append(mouton)
    def saute_rep(troupeau1:list, troupeau2:list):
        for i in range(len(troupeau1)):
            MOUTON=troupeau1.pop()
            troupeau2.append(MOUTON)
class pb1q3(Tot):
    def element_central(lst):
        "précondition : lst est une liste non vide"
        n=len(lst)
        return lst[n/2]
    def element_central_rep(lst):
        "précondition : lst est une liste non vide"
        n=len(lst)
        return lst[n//2]
class pb1q4(Tot):
    def double_lists(tab1,tab2):
        i=0
        while i<len(tab1) or i<len(tab2):
            tab1[i]=tab1[i]-tab2[i]
            i+=1
    def double_lists_rep(tab1,tab2):
        i=0
        while i+1<len(tab1) or i+1<len(tab2):
            print(tab1,tab2)
            tab1[i]=tab1[i]-tab2[i]
            i+=1
class pb1q5(Tot):
    def est_present(lst,x):
        for e in lst:
            if e==x:
                return True
        return False
    def est_present_rep(lst,x):
        for e in lst:
            if str(e)==str(x):
                return True
        return False
class pb1q6(Tot):
    def egal():
        a=0.1
        b=0.2
        if (a+b)==0.3:
            print("Ok")
            return "Ok"
        else:
            print("pas egal")
            return "pas egal"
    def egal_rep():
        a=0.1
        b=0.2
        if (a+b)==0.30000000000000004:
            print("Ok")
            return "Ok"
        else:
            print("pas egal")
            return "pas egal"
class pb3q1(Tot):
    def recherche_dichotomique(tab,val):
        gauche=0
        i=0
        droite=len(tab)-1
        while gauche <= droite:
            print("i={}".format(i))
            milieu=(gauche+droite)//2
            if tab[milieu]==val:
                print("tab[milieu]={}".format(tab[milieu]))
                return milieu
            elif tab[milieu]>val:
                droite=milieu-1
                print("tab[milieu]={}".format(tab[milieu]))
            else:
                gauche=milieu+1
                print("tab[milieu]={}".format(tab[milieu]))
            i+=1
        #on est sorti de la boucle sans trouver val
        return -1

    def dicho_trace(T,X,milieu,droite):
        if X>T[milieu]:
            print(T[milieu])
            res=pb3q1.dicho_trace(T,X,milieu+1,droite)
            print("Droite=",droite)
            print("retour",res)
            return res
        else:
            print(T[milieu])
            res=pb3q1.dicho_trace(T,X,gauche,milieu-1)
            print("Gauche=",gauche)
            print("retour",res)
            return res

def launch():
    tab=[1,4,7,8,9,27,28,30,32,99,105,110,115,200,210,220]
    val=115
    print("recherche de ",val)
    resultat=pb3q1.recherche_dichotomique(tab,val)
    print("Position=",resultat)
    tab=list(range(200))
    val=5000
    print("recherche de ",val)
    resultat=pb3q1.recherche_dichotomique(tab,val)
    print("Position=",resultat)
    ma_liste=[1,4,7,8,9,27,28,30,32,99,105,110,115,200,210]
    pb3q1.dicho_trace(ma_liste,val,0,len(ma_liste)-1)
TI=Tot()
print("1 pyramide_inversee(n)                   2 pyramide_inversee_rep(n)")
print("3 saute(troupeau1:list, troupeau2:list)  4 saute_rep(troupeau1, troupeau2)")
print("5 element_central(list1)                 6 element_central(list1)")
print("7 double_lists(list1,list2)              8 double_lists_rep(list1,list2)")
print("9 est_present(lst,x)                    10 est_present_rep(lst,x)")
print("11 egal()                               12 egal_rep()")
print("13 recherche_dichotomique(tab,val)      14 recherche_dichotomique(list(range(200)),val)")
print("15 dicho_trace(ma_liste,val,0,len(ma_liste)-1)")
funct=input("Entrez le numéro de la def que vous souhaitez exécuter:")
a=int(funct)
if a==1:
    print("in a==1")
    TI.pic=0
    b=input("Entrez n:")
    b=int(b)
    pb1q1.pyramide_inversee(b)
elif a==2:
    print("in a==2")
    TI.pic=0
    b=input("Entrez n:")
    b=int(b)
    pb1q1.pyramide_inversee_rep(b)
elif a==3:
    list1,list2=[],[]
    times=int(input("Entrez le nombre de chiffres pour liste 1:"))
    for i in range(times):list1.append(int(input("Entrez l'élément {} de la liste 1:".format(i+1))))
    times=int(input("Entrez le nombre de chiffres pour liste 2:"))
    for i in range(times):list2.append(int(input("Entrez l'élément {} liste 2:".format(i+1))))
    print(pb1q2.saute(list1,list2))
    print("liste1={}\nliste2={}".format(list1,list2))
elif a==4:
    list1,list2=[],[]
    times=int(input("Entrez le nombre de chiffres pour liste 1:"))
    for i in range(times):list1.append(int(input("Entrez l'élément {} de la liste 1:".format(i+1))))
    times=int(input("Entrez le nombre de chiffres pour liste 2:"))
    for i in range(times):list2.append(int(input("Entrez l'élément {} liste 2:".format(i+1))))
    print(pb1q2.saute_rep(list1,list2))
    print("liste1={}\nliste2={}".format(list1,list2))
elif a==5:
    list1=[]
    times=int(input("Entrez le nombre de chiffres pour liste 1:"))
    for i in range(times):list1.append(int(input("Entrez l'élément {} de la liste 1:".format(i+1))))
    print(pb1q3.element_central(list1))
    print("liste1={}".format(list1))
elif a==6:
    list1=[]
    times=int(input("Entrez le nombre de chiffres pour liste 1:"))
    for i in range(times):list1.append(int(input("Entrez l'élément {} de la liste 1:".format(i+1))))
    print(pb1q3.element_central_rep(list1))
    print("liste1={}".format(list1))
elif a==7:
    list1,list2=[],[]
    times=int(input("Entrez le nombre de chiffres pour liste 1:"))
    for i in range(times):list1.append(int(input("Entrez l'élément {} de la liste 1:".format(i+1))))
    times=int(input("Entrez le nombre de chiffres pour liste 2:"))
    for i in range(times):list2.append(int(input("Entrez l'élément {} liste 2:".format(i+1))))
    print(pb1q4.double_lists(list1,list2))
    print("liste1={}\nliste2={}".format(list1,list2))
elif a==8:
    list1,list2=[],[]
    times=int(input("Entrez le nombre de chiffres pour liste 1:"))
    for i in range(times):list1.append(int(input("Entrez l'élément {} de la liste 1:".format(i+1))))
    times=int(input("Entrez le nombre de chiffres pour liste 2:"))
    for i in range(times):list2.append(int(input("Entrez l'élément {} liste 2:".format(i+1))))
    print(pb1q4.double_lists_rep(list1,list2))
    print("liste1={}\nliste2={}".format(list1,list2))
elif a==9:
    list1=[]
    x=int(input("Entrez le nombre recherché:"))
    times=int(input("Entrez le nombre de chiffres pour liste 1:"))
    for i in range(times):list1.append(int(input("Entrez l'élément {} de la liste 1:".format(i+1))))
    print(pb1q5.est_present(list1,x))
    print("liste1={}".format(list1))
elif a==10:
    list1=[]
    x=int(input("Entrez le nombre recherché:"))
    times=int(input("Entrez le nombre de chiffres pour liste 1:"))
    for i in range(times):list1.append(int(input("Entrez l'élément {} de la liste 1:".format(i+1))))
    print(pb1q5.est_present_rep(list1,x))
    print("liste1={}".format(list1))
elif a==11:
    print("egal?:{}".format(pb1q6.egal()))
elif a==12:
    print("egal?:{}".format(pb1q6.egal_rep()))
elif a==13:
    tab=[1,4,7,8,9,27,28,30,32,99,105,110,115,200,210,220]
    val=115
    print("recherche de ",val)
    resultat=pb3q1.recherche_dichotomique(tab,val)
    print("Position=",resultat)
elif a==14:
    tab=list(range(200))
    val=5000
    print("recherche de ",val)
    resultat=pb3q1.recherche_dichotomique(tab,val)
    print("Position=",resultat)
elif a==15:
    ma_liste=[1,4,7,8,9,27,28,30,32,99,105,110,115,200,210]
    val=115
    pb3q1.dicho_trace(ma_liste,val,0,len(ma_liste)-1)
#.
