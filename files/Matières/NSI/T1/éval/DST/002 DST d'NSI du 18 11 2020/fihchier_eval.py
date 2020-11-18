class ev:
    def __init__(self):
        self.t=[0]*8
    def rendu_monnaie(pieces,s) :
        """renvoie le nombre minimal de pièces pour faire la somme s avec le système pièces"""
        if s==0:
            return 0
        r=s #s=1+1+...+1 dans le pire des cas
        for p in pieces:
            if p<=s:
                r = min ( r , 1 + ev.rendu_monnaie (pieces,s-p))
        return r
    def rendu_monnaie2(pieces,s) :
        """renvoie le nombre minimal de pièces pour faire la somme s avec le système pièces"""
        nb=[0]*(s+1) 
        for n in range(1,s+1):
            nb[n]=n #n=1+1+1+...+1 dans le pire des cas
            for p in pieces:
                if p <=n:
                    nb[n]=min(nb[n],1+nb[n-p])
        return nb[s]
    def rendu_monnaie3(pieces,s) :
        """renvoie le nombre minimal de pièces pour faire la somme s avec le système pièces"""
        nb=[0]*(s+1) 
        for n in range(1,s+1):
            nb[n]=n#n=1+1+1+...+1 dans le pire des cas
            for p in pieces:
                if p <=n:
                    nb[n]=max(nb[n],1+nb[n-p])
        return nb[s]
    def aligne_sequence(s1,s2):
        """Le score du meilleur alignement de s1 et s2"""
        GE=[" ","G","E","N","O","M","E"]
        n1,n2=len(s1),len(s2)
        sc=[[0]*(n2+1) for _ in range(n1+1)]
        for i in range(1,n1+1):sc[i][0]=-i
        for j in range(1,n2+1):sc[0][j]=-j
        for i in range(1,n1+1):
            for j in range(1,n2+1):
                s=max(-1+sc[i-1][j],-1+sc[i][j-1])
                if s1[i-1]==s2[j-1]: sc[i][j]=max(s,1+sc[i-1][j-1])
                else: sc[i][j]=max(s,-1+sc[i-1][j-1])
                print("E   N   O   R   M   E")
        for b in range(len(sc)):
            for f in range(len(sc[b])):
                length=len("{}".format(sc[b][f]))
                if length==1: print("| {}".format(sc[b][f]),end=" ")
                else: print("|{}".format(sc[b][f]),end=" ")
            print("|",end="")
            print("{}".format(GE[b]))
        return sc[n1][n2]
    def aligne_sequence2(s1,s2):
        """Le score du meilleur alignement de s1 et s2"""
        GE=[" ","G","E","N","O","M","E"]
        n1,n2=len(s1),len(s2)
        sc=[[0]*(n2+1) for _ in range(n1+1)]
        for i in range(1,n1+1):sc[i][0]=-i
        for j in range(1,n2+1):sc[0][j]=-j
        print("E   N   O   R   M   E")
        for i in range(1,n1+1):
            print("{}".format(GE[b]),end="")
            for j in range(1,n2+1):
                s=max(-1+sc[i-1][j],-1+sc[i][j-1])
                if s1[i-1]==s2[j-1]: sc[i][j]=max(s,1+sc[i-1][j-1])
                else: sc[i][j]=max(s,-1+sc[i-1][j-1])
                print("|{:>3}".format(sc[i][j]),end=" ")
            print()
        return sc[n1][n2]

    def fibod(n):
        N1=[0]
        N2=[0]
        while n>0:
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
                    return (ev.fibod(n-1)+ev.fibod(n-2))
                else:
                    return n
    def fibo2(n):
        fist=[0]
        if n==0 or n==1: return n
        else:
            for i in range(len(fist)):
                if ((n-1)+(n-2))==fist[i]:continue
                else:
                    fist.append((n-1)+(n-2))
                    return ev.fibo2(n-1)+ev.fibo2(n-2)
    def fibo3(self,n):
        print(self.t)
        print(n)
        if n==0 or n==1:
            self.t[n]=n
            return n
        if self.t[n]>0:
            return self.t[n]
        self.t[n]=ev.fibo3(self,n-1)+ev.fibo3(self,n-2)
        print(self.t)
        return (self.t[n])
        






word1="ENORME"
word2="GENOME"
#L’appel
print(ev.rendu_monnaie([1,2],3))
print(ev.rendu_monnaie2([1,6,10],12))
print(ev.rendu_monnaie([1,6,10],12))
print(ev.aligne_sequence(word2,word1))
word1="-ENORME"
word2="GENO-ME"
print(ev.aligne_sequence2(word2,word1))
print(ev.fibod(7))
EV=ev()
print("t={}".format(EV))
print("resultat={}".format(ev.fibo2(EV,7)))
print("t={}".format(EV))
print ("Créé par henry Letellier")