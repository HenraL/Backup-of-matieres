def rendu_monnaie_mem(P,X):
    mem=[0]*(X+1)
    return rendu_monnaie_mem_c(P,X,mem)

def rendu_monnaie_mem_c(P,X,m):
    if X==0:return 0
    elif m[X]>0:return m[X]
    else:
        mini=X+1
        for i in range(len(P)):
            if P[i]<=X:
                nb=1+rendu_monnaie_mem_c(P,X-P[i],m)
                if nb<mini:
                    mini=nb
                    m[X]=mini
    return mini

somme=1000001
liste_pieces=[1545,574,56,45,40,10,2]
print(rendu_monnaie_mem(liste_pieces,somme))

# somme=10000012251
# liste_pieces=[83,79,61,60,58,57,50,25,24,23,22,21,13,11,5]

# print(rendu_monnaie_mem(liste_pieces,somme)) #ne marcheras pas car ondépasse la capacité de calcul de python