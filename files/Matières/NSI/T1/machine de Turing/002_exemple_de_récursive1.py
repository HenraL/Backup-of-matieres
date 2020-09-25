def transition2(ruban,i,etat):
    if etat==1:
        if ruban[i]==None:
            ruban[i]=1
    elif etat==2:
        if ruban[i]==None:
            ruban[i]=0

def machine2(ruban):
    i,e=0,1
    etats=[2,1]
    while i<len(ruban):
        transition2(r,i,e)
        i=i+1
        e=etats[e-1]

r=20*[None]
machine2(r)
print(r)
