def DPBUChange(S,X):
    print("initialisation")
    track=[0]*(X+1)
    keep=[0]*(X+1)
    coin=0
    print("calculs...")
    for x in range(1,X+1):
        mini=X+1
        for i in range(len(S)):
            if (S[i]<=x) and (1+track[x-S[i]]<mini):
                mini=1+track[x-S[i]]
                coin=i
        track[x]=mini
        keep[x]=coin
    x,L=X,[]

    print("je suis ici")
    while x>0:
        L.append(S[keep[x]])
        x-=S[keep[x]]
    return track[X],L

S=(1,2,5,10,20)
print(DPBUChange(S,8))

somme=1000001
liste_pieces=(1545,574,56,45,40,10,2)
liste_pieces=(2,10,40,45,56,574,1545)

print(DPBUChange(liste_pieces,somme))