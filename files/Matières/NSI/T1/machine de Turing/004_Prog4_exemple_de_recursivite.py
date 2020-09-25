def machine1(ruban,i,etat):
    if i<len(ruban):
        if etat==1:
            if ruban[i]==None:
                machine1(ruban, i+1,2)
            else:
                machine1(ruban,i,2)
        elif etat==2:
            if ruban[i]==0:
                ruban[i]=1
                machine1(ruban, i+1,2)
        elif ruban[i]==1:
            ruban[i]=0
            machine1(ruban,i+1,2)
        else:
            i=len(ruban)
r=20*[None]
machine1(r,0,1)
print(r)
