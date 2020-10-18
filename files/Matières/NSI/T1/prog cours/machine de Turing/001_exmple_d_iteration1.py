def machine2(ruban, i, etat):
    while i<len(ruban):
        if etat==1:
            if ruban[i]==None:
                ruban[i]=1
                i+=1
                etat=2
        elif etat==2:
            if ruban[i]==None:
                ruban[i]=0
                i+=1
                etat=1
        else:
            i=len(ruban) #utile s'il y a une erreur sur l'état initial

#Pour tester
r=20*[None]
machine2(r,0,1)
print(r)