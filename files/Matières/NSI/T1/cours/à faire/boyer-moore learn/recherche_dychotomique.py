#Recherche Dychotomique ou tri-fusion




class mains:
    def __init__(self):
        self.a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,1,17,18,19,20]
        self.b=[]
        self.mid_a=""
        self.mid_b=""
        
    def append_list(self):
        for i in range(len(self.a)-2):
            self.b.append(a[i])
    def get_terms():
        a=""
        ng=True
        while ng==True:
            A=input("Entrez le nombre recherché:")
            try:
                A=int(A)
                ng=False
            except:
                print("Merci de ne rentrer qu'un nombre et non des lettres")
        return A
    def dicho(self,L,a,i):
        i+=1
        print("i={}".format(i))
        print("L={}".format(L))
        if len(L)==1:
            print("in len(L)==1")
            m=L[0]
            print("m={}".format(m))
            if m!=a:
                print("m!=a={}".format(m!=a))
                assert "'{}' n'est pas dans la liste".format(m)
        n=((len(L)-1)//2)
        m=L[n]
        print("m={}".format(m))
        if m==a:
            print("in m==a")
            print("L={}".format(L))
            print("n={}".format(n))
            #return "Le résultat cherché est {}".format(str(n))
        elif m>a:
            print("m>a")
            return ((n+1)+(mains.dicho(self,L[0:(n-1)],a,i)))
        else:
            print("m<a")
            print("L={}".format(L))
            return ((n-1)+(mains.dicho(self,L[(n+1):len(L)],a,i)))






MI=mains()
#MI.append_list()
for b in range(1,len(MI.a)):
    c=mains.dicho(MI,MI.a,MI.a[b],0)#mains.get_terms())
    print(c)
#mains

#self.mid_b=((len(b)-1)//2)


#get_term_for_a=get_terms
#get_term_for_b=get_terms
