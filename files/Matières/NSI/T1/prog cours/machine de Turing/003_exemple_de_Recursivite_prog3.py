def machine2(ruban, i, etat):
    if i<len(ruban):
        if etat==1:
            if ruban[i]==None:
                ruban[i]=1
                machine2(ruban, i+1,2)
        elif etat==2:
            if ruban[i]==None:
                ruban[i]=0
                machine2(ruban,i+1,1)

r=20*[None]
machine2(r,0,1)
print(r)
